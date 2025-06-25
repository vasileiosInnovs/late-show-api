

````markdown
# late-show-api

A RESTful API built with Flask, SQLAlchemy, PostgreSQL, and JWT Authentication.

---

## 📦 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/vasileiosInnovs/late-show-api
cd late-show-api
````

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the App

### 1. Initialize and migrate the database

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
export FLASK_APP=server.app:create_app
export FLASK_ENV=development
flask run
# or with gunicorn
gunicorn "server.app:create_app()"
```

---

## 🔐 Authentication Flow

### Register a new user

* `POST /register`
* Request body:

```json
{
  "username": "alice",
  "password": "secret123"
}
```

### Log in to receive a JWT

* `POST /login`
* Response:

```json
{
  "access_token": "k4jN8D2lZ9xR3T7vQ1mS6aB0cE5wU8fG"
}
```

### Use token in protected routes



```
Authorization: Bearer k4jN8D2lZ9xR3T7vQ1mS6aB0cE5wU8fG
```

---

## 🧭 Route List

| Method | Endpoint             | Auth Required | Description                     |
| ------ | -------------------- | ------------- | ------------------------------- |
| POST   | `/register`          | ❌             | Register a new user             |
| POST   | `/login`             | ❌             | Log in and receive JWT          |
| GET    | `/check_session`     | ✅             | Get current user from token     |
| POST   | `/appearances`       | ✅             | Create a new appearance         |
| DELETE | `/episodes/<int:id>` | ✅             | Delete an episode and its links |
| GET    | `/episodes`          | ❌             | List all episodes               |
| GET    | `/episodes/<int:id>` | ❌             | Get episode details and guests  |
| GET    | `/guests`            | ❌             | List all guests                 |

---

## 💡 Sample Request with Token (using Postman or Curl)

```bash
curl -X POST http://localhost:5000/appearances \
  -H "Authorization: Bearer your.jwt.token" \
  -H "Content-Type: application/json" \
  -d '{"rating": 5, "guest_id": 1, "episode_id": 2}'
```

---

## 📬 Postman Usage

### 1. Import Collection

* Open Postman
* Click **"Import"** → **"Upload Files"**
* Select the provided `.json` collection (or create your own)

### 2. Set environment variable

* Add a variable called `token` and paste your JWT token there
* Use `Bearer {{token}}` in Authorization headers for protected routes

---

## 🔗 GitHub Repository

[https://github.com/vasileiosInnovs/late-show-api](https://github.com/vasileiosInnovs/late-show-api)

---

## 🛠 Tech Stack

* Python 3.11
* Flask + Flask-Restful
* Flask-JWT-Extended
* SQLAlchemy + PostgreSQL
* Flask-Migrate

```

