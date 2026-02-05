# FastAPI Boilerplate

A clean, minimal FastAPI boilerplate with user authentication.

## Features

- User registration and login (email/password)
- JWT-based authentication with session management
- SQLAlchemy ORM with Alembic migrations
- Clean layered architecture (router → service → crud → model)
- Frontend-friendly error responses

## Project Structure

```
app/
├── core/           # Config, database, security, middleware
├── crud/           # Data access layer
├── model/          # SQLAlchemy models
├── router/         # API endpoints (versioned at /api/v1/)
├── schema/         # Pydantic schemas
├── service/        # Business logic
├── session/        # Session management
└── utils/          # Helpers (hashing, jwt)
```

## Quick Start

1. Clone and create virtual environment:
```bash
git clone <repo-url>
cd fastapi-boilerplate
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment:
```bash
cp .env.example .env
# Edit .env with your database credentials
```

4. Run migrations (production) or set DEBUG=true for auto-create:
```bash
alembic upgrade head
```

5. Start the server:
```bash
python main.py
```

6. Open http://localhost:8000/docs for Swagger UI

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/auth/register` | Register new user |
| POST | `/api/v1/auth/login` | Login, get JWT |
| POST | `/api/v1/auth/logout` | Logout (invalidate token) |
| GET | `/api/v1/users/me` | Get current user profile |
| GET | `/health` | Health check |

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| DB_HOST | Yes | - | Database host |
| DB_PORT | No | 5432 | Database port |
| DB_NAME | Yes | - | Database name |
| DB_USER | Yes | - | Database user |
| DB_PASS | Yes | - | Database password |
| SECRET_KEY | Yes | - | JWT secret key |
| DEBUG | No | false | Enable debug mode (auto-creates tables) |

## Extending

- Add new models in `app/model/`
- Add CRUD operations in `app/crud/`
- Add business logic in `app/service/`
- Add endpoints in `app/router/api/v1/`
- Add custom exceptions in `app/core/exceptions.py`

## Notes

- Session storage is in-memory (swap to Redis for production scaling)
- Password hashing uses PBKDF2 (swap to bcrypt/argon2 as needed)
- Set `DEBUG=false` in production and use Alembic migrations
