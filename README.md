# 🚀 LearnSync

LearnSync is a backend application built with **FastAPI** to help users organize and manage everything they are learning in one place. It allows users to create learning spaces, save resources, write notes, track revisions, organize content with tags, and view learning analytics.

The project follows a clean folder structure and uses JWT authentication to secure protected APIs.

---

## ✨ Features

- User Registration & Login (JWT Authentication)
- Create and Manage Learning Spaces
- Add Learning Resources
- Create Notes
- Organize Resources with Tags
- Search and Filter Resources
- Revision Tracking
- Analytics Dashboard
- RESTful APIs
- Swagger Documentation
- Unit Testing with Pytest

---

## 🛠 Tech Stack

- FastAPI
- Python
- PostgreSQL (Neon)
- SQLAlchemy ORM
- Pydantic
- JWT Authentication
- Passlib (Password Hashing)
- Pytest
- Render (Deployment)

---

## 📂 Project Structure

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

## 🌐 Live Demo

**Base URL**

```
https://learnsync-judt.onrender.com
```

**Swagger Documentation**

```
https://learnsync-judt.onrender.com/docs
```
>**Tip:** Use **Postman** to authenticate and test protected APIs by adding the JWT as a **Bearer Token**.
---

## 🔐 Authentication

The project uses **JWT (JSON Web Tokens)** for authentication. 

1. Register a new user.
2. Login to receive an access token.
3. Use the token as a Bearer Token for protected endpoints.

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
git clone https://github.com/<palak0013>/LearnSync.git
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

## 📊 Current Features

- JWT Authentication
- CRUD Operations
- Search & Filtering
- Notes Management
- Resource Tagging
- Revision Scheduling
- Analytics Dashboard
- Automated Testing
- Live Deployment

---


