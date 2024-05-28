![intlle_docs](https://github.com/Intlle/Backend/assets/146841763/38772e5d-8c51-41f0-81cd-b3c1b0a3afe0)
## Intlle Backend Documentation
[![en](https://img.shields.io/badge/lang-en-blue.svg)](https://github.com/Intlle/Backend/blob/docs-update/README.md)

## Структура файлов

Проект имеет следующую структуру файлов:

```
Intlle Backend
├── README.md
├── requirements.txt
└── src
    ├── config.py
    ├── db.py
    ├── main.py
    ├── migrations.py
    ├── models.py
    ├── routers.py
    └── schemas.py

```

- `src/main.py`: Этот файл является точкой входа в приложение. Он создает экземпляр приложения FastAPI и настраивает маршруты и обработчики запросов.

- `src/config.py`: Этот файл содержит переменные конфига проекта.

- `src/db.py`: Этот файл содержит движок и функцию для создания сессий базы данных.

- `src/migrations.py`: Этот файл содержит код для создания базы данных.

- `src/models.py`: Этот файл содержит модельки для таблиц базы данных.

- `src/routers.py`: Этот файл содержит CRUD роутеры для проекта.

- `src/schemas.py`: Этот файл содержит схемы Pydantic.

- `requirements.txt`: Этот файл содержит список зависимостей Python, необходимых для запуска приложения.

- `README.md`: Этот файл содержит документацию по проекту.


## Маршруты

- `/create` Данный роутер создает новую карточку
- `/get/{node_id}` Данный роутер возвращает карточку по id
- `/get` Данный роутер возвращает все карточки
- `/update/{node_id}` Данный роутер обновляет карточку по id
- `/delete/{node_id}` Данный роутер удаляет карточку по id

## Запуск
Для запуска проекта необходимо открыть папку проекта и в терминале написать команду:

```bash
uvicorn src.main:app --reload
```
