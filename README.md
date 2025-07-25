# 🧠 AIFlow Builder – Backend

This is the backend API for **AIFlow Builder**, built with **FastAPI**. It handles user authentication, flow management, and other core logic.

---

## 🚀 Tech Stack

- **Python 3.11+**
- **FastAPI**
- **Pydantic**
- **Uvicorn**
- **Poetry** (for dependency management)
- **JWT** authentication
- **SQLAlchemy / Tortoise / your ORM**

---

## 🛠 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/FrankDannie/AIFlow_Builder-BE.git
```
2. Install Dependencies
```bash
poetry install
```
3. Set up Environment Variables
Create a .env file:

```bash
JWT_SECRET=your_jwt_secret
DATABASE_URL=sqlite:///./db.sqlite3
```
4. Run the Server
```bash
poetry run poe dev
```
📦 API Endpoints

- Method	Endpoint	Description
- POST	/api/auth/signup	Register new users
- POST	/api/auth/login	Get JWT token

For full docs, visit http://localhost:8000/docs.

🧪 Testing
```bash
poetry run pytest
```
