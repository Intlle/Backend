import uuid
from src.models import User
from src.schemas import Nodes, UserSchema
from src.db import get_session
from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import Response
from sqlalchemy import select, delete, update

router = APIRouter()


@router.post("/create")
async def create_user(nodes: Nodes, session: AsyncSession = Depends(get_session)) -> Response:
    'Создает пользователя'
    try:
        user = User(id=str(uuid.uuid4()), nodes=nodes.nodes)
        session.add(user)
        await session.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return Response(status_code=201, content="User created")


@router.get("/get/{node_id}")
async def get_by_id(node_id: str, session: AsyncSession = Depends(get_session)) -> Nodes:
    'Возвращает node по id'
    try:
        query = select(User).where(User.id == node_id)
        raw = await session.execute(query)
        res = raw.scalars().first()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    if res is None:
        raise HTTPException(status_code=404, detail="Node not found")

    return Nodes(nodes=res.nodes)


@router.get("/get")
async def get_all(session: AsyncSession = Depends(get_session)) -> list[UserSchema]:
    'Возвращает все node'
    try:
        query = select(User)
        raw = await session.execute(query)
        res = raw.scalars().all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    if not res:
        raise HTTPException(status_code=404, detail="Nodes not found")

    return [UserSchema(id=user.id, nodes=user.nodes) for user in res]


@router.put("/update/{node_id}")
async def update_by_id(node_id: str, nodes: Nodes, session: AsyncSession = Depends(get_session)) -> Response:
    'Обновляет пользователя по id'
    try:
        query = update(User).where(User.id == node_id).values(nodes=nodes.nodes)
        res = await session.execute(query)
        await session.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    if res.rowcount == 0:
        raise HTTPException(status_code=404, detail="Node not found")

    return Response(status_code=200, content="User updated")


@router.delete("/delete/{node_id}")
async def delete_by_id(node_id: str, session: AsyncSession = Depends(get_session)) -> Response:
    'Удаляет пользователя по id'
    try:
        query = delete(User).where(User.id == node_id)
        res = await session.execute(query)
        await session.commit()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    if res.rowcount == 0:
        raise HTTPException(status_code=404, detail="Node not found")

    return Response(status_code=200, content="User deleted")