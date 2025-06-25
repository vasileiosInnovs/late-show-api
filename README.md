# late-show-api

A RESTful API built with Flask, SQLAlchemy, PostgreSQL, and JWT Authentication.

---

## Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/vasileiosInnovs/late-show-api
cd late-show-api
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the App

### 1. Initialize and migrate the database

> 💡 Skip `flask db init` if migrations are already initialized.

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 2. Seed the database (optional)

```bash
python seed.py
```

### 3. Start the server

```bash
export FLASK_APP=app.py
export FLASK_RUN_PORT=5000
flask run
```
---

## Authentication Flow

### Register a new user

* `POST /register`
* Request body:

```json
{
  "username": "alice",
  "password": "secret123"
}
```

### ✅ Log in to receive a JWT

* `POST /login`
* Response:

```json
{
  "access_token": "<JWT_TOKEN>"
}
```

### ✅ Use the token in protected routes

Set the token in the `Authorization` header:

```
Authorization: Bearer <JWT_TOKEN>
```

---

## Route List

| Method | Endpoint             | Auth Required | Description                     |
|--------|----------------------|----------------|---------------------------------|
| POST   | `/register`          | ❌             | Register a new user             |
| POST   | `/login`             | ❌             | Log in and receive JWT          |
| POST   | `/appearances`       | ✅             | Create a new appearance         |
| DELETE | `/episodes/<int:id>` | ✅             | Delete an episode and its links |
| GET    | `/episodes`          | ❌             | List all episodes               |
| GET    | `/episodes/<int:id>` | ❌             | Get episode details and guests  |
| GET    | `/guests`            | ❌             | List all guests                 |

---

## 💡 Sample Request with Token (cURL)

```bash
curl -X POST http://localhost:5000/appearances \
  -H "Authorization: Bearer <your.jwt.token>" \
  -H "Content-Type: application/json" \
  -d '{"rating": 5, "guest_id": 1, "episode_id": 2}'
```

---

## Using Postman

### 1. Import the Collection

- Open Postman
- Click **"Import"** → **"Upload Files"**
- Select the provided `.json` collection (or create one manually)

### 2. Set Environment Variable

- Add an environment variable named `token`
- Paste your JWT token as the value
- Use `Bearer {{token}}` in the **Authorization** header for protected routes

---

## 🔗 GitHub Repository

[https://github.com/vasileiosInnovs/late-show-api](https://github.com/vasileiosInnovs/late-show-api)

---

## 🛠 Tech Stack

- Python 3.11
- Flask + Flask-RESTful
- Flask-JWT-Extended
- SQLAlchemy + PostgreSQL
- Flask-Migrate