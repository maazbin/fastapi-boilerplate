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

3. Create `.env` file in project root:
```env
# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=dbname
DB_USER=user
DB_PASS=password

# Security
SECRET_KEY=your-secret-key-change-in-production

# Optional (defaults shown)
# ALGORITHM=HS256
# ACCESS_TOKEN_EXPIRE_MINUTES=30
# DEBUG=false
# PROJECT_NAME=FastAPI App
# CORS_ORIGINS=["http://localhost:3000"]
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
| ALGORITHM | No | HS256 | JWT algorithm |
| ACCESS_TOKEN_EXPIRE_MINUTES | No | 30 | Token expiry |
| PROJECT_NAME | No | FastAPI App | App name |
| CORS_ORIGINS | No | ["http://localhost:3000"] | Allowed origins |

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
