# 📚LearnSync

LearnSync is a backend-first personal learning management system built with **FastAPI**.

The idea is simple: learning information is often scattered across different platforms — courses, YouTube videos, documentation, GitHub repositories, notes, coding platforms, personal projects, and revision plans.

LearnSync provides a centralized backend for organizing and tracking these parts of a learning journey through REST APIs.

The project is primarily focused on applying practical **backend engineering concepts** rather than building a large frontend application.

---

## 🚀Live Demo

**Application**

[LearnSync](https://learnsync-judt.onrender.com)

**API Documentation**

[Swagger UI](https://learnsync-judt.onrender.com/docs)

**ReDoc**

[ReDoc](https://learnsync-judt.onrender.com/redoc)

The deployed API can be explored and tested directly through Swagger UI.

---

## ✨Features

- User Registration & Login with JWT Authentication
- Create and Manage Learning Spaces
- Add and Manage Learning Resources
- Create and Manage Notes
- Organize Resources with Tags
- Search and Filter Resources
- Revision Scheduling and Tracking
- Analytics Dashboard
- RESTful APIs
- Interactive Swagger Documentation
- Automated Testing with Pytest

---

## 🛠️Tech Stack

- Python
- FastAPI
- PostgreSQL (Neon)
- SQLAlchemy ORM
- Pydantic
- JWT Authentication
- Passlib / bcrypt for Password Hashing
- Pytest
- Render for Deployment

---

## 🗂️Project Structure

```text
LearnSync/
│
├── api/
├── crud/
├── database/
├── models/
├── schemas/
├── utils/
├── tests/
├── main.py
├── requirements.txt
└── README.md
```
---

## 🔒Authentication

LearnSync uses JWT (JSON Web Tokens) for authentication and protects endpoints that require an authenticated user.

**Using Swagger for Authentication**

1. Open the [Swagger UI](https://learnsync-judt.onrender.com/docs).
2. Register a new user using `/auth/register`.
3. Login using `/auth/login`.
4. Copy the returned JWT access token.
5. Click the `Authorize` button in Swagger.
6. Enter the token.
7. Test the protected endpoints directly from the browser.

---

## 📌 API Modules

- Authentication
- Learning Spaces
- Learning Resources
- Notes
- Tags
- Search & Filters
- Revision System
- Analytics Dashboard

---

## 🧪 Running Locally

Clone the repository:

```bash
git clone https://github.com/palak0013/LearnSync.git
```

Move into the project:

```bash
cd LearnSync
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your database credentials:

```env
DATABASE_URL=your_neon_database_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Run the application:

```bash
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## 🌐API Workflow
```text
Register User
     ↓
Login
     ↓
Receive JWT Token
     ↓
Authorize Swagger
     ↓
Create Learning Space
     ↓
Add Learning Resources
     ↓
Create Notes
     ↓
Organize Resources with Tags
     ↓
Schedule Revisions
     ↓
View Analytics
```
---
## ⚡Backend Concepts Demonstrated
This project demonstrates practical experience with:

- REST API design
- FastAPI
- JWT authentication
- Password hashing
- Protected API endpoints
- CRUD operations
- SQLAlchemy ORM-
- PostgreSQL
- Database relationships
- Pydantic validation
- Dependency injection
- API documentation with OpenAPI
- Automated testing with Pytest
- Backend deployment

---


## 📈Project Status
LearnSync is currently focused on its core backend functionality.

The project is intentionally kept simple while focusing on applying fundamental backend engineering concepts using FastAPI, PostgreSQL, authentication, and REST APIs.

---



