from pydantic import BaseModel



class UserSchema(BaseModel):
    id: str
    nodes: str


class Nodes(BaseModel):
    nodes: str




class Response(BaseModel):
    status: int