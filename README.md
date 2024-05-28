![intlle_docs](https://github.com/Intlle/Backend/assets/146841763/38772e5d-8c51-41f0-81cd-b3c1b0a3afe0)
## Intlle Backend Documentation
[![ru](https://img.shields.io/badge/lang-ru-blue.svg)](https://github.com/Intlle/Backend/blob/docs-update/README.ru.md)
### File structure
```
Backend
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

- `src/main.py` - program's entry point, makes a fastAPI application instance and sets up all the routes and requests handlers. 

- `src/config.py` - project's configuration variables.

- `src/db.py` - contains database engine and a function to create database sessions.

- `src/migrations.py` - database creation code.

- `src/models.py` - database' models code.

- `src/routers.py` - contains all of the application's CRUD routers.

- `src/schemas.py` - contains Pydantic schemes.

- `requirements.txt` - a list of project's dependencies.

- `README.md` - project's documentation file.

### Application routes
- `/create` - creates new entry in the main database (data for the entry is passed in request's body as ```{'nodes' : 'string'}```; returns entry's assigned UUID in response)

- `/update/{node_id}` - updates database entry by its UUID

- `/delete/{node_id}` - deletes database entry by its UUID

- `/get/{node_id}` - returns database entry's data by its UUID

- `/get` - returns all the entries in the database

### Launching the project (in development mode)
1) Open project's folder through the system's terminal
2) Install project's dependencies:
```bash
pip install -r requirements.txt
```
3) Launch the development server for the project:
```bash
uvicorn src.main:app --reload
```
