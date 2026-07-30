# LearnSync

LearnSync is a backend application built with FastAPI for organizing learning resources, notes, revision schedules, and progress tracking. It provides a secure REST API with JWT authentication and follows a modular backend architecture.

## Features

- User authentication with JWT
- Learning Spaces management
- Learning Resources CRUD
- Notes management
- Resource tagging
- Search and filtering
- Revision scheduling
- Analytics dashboard
- API testing with Pytest

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- JWT Authentication
- Passlib
- Pytest

## Project Structure

```
LearnSync
├── api/
├── crud/
├── database/
├── models/
├── schemas/
├── tests/
├── utils/
├── main.py
├── requirements.txt
└── README.md
```

## Authentication

Protected endpoints require a JWT access token.

1. Register a user.
2. Login using `/auth/login`.
3. Copy the returned `access_token`.
4. Use the token as a Bearer token when accessing protected endpoints.

## Setup

Clone the repository.

```bash
git clone https://github.com/your-username/LearnSync.git
cd LearnSync
```

Create a virtual environment.

```bash
python -m venv venv
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Create a `.env` file.

```env
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Run the application.

```bash
uvicorn main:app --reload
```

## API Documentation

After starting the server, visit:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Testing

Run the test suite using:

```bash
python -m pytest
```
