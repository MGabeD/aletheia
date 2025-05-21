# Aletheia Backend

A FastAPI backend with Google OAuth authentication.

## Setup

1. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up environment variables in a `.env` file:

```
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_client_secret
GOOGLE_REDIRECT_URI=http://localhost:8000/auth/callback
```

## Running the Server

Start the server with:

```bash
uvicorn main:app --reload
```

The server will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:

- Swagger UI documentation: `http://localhost:8000/docs`
- ReDoc documentation: `http://localhost:8000/redoc`

## Authentication Flow

1. Frontend calls `/auth/login` to get the Google OAuth URL
2. User is redirected to Google for authentication
3. Google redirects back to `/auth/callback` with an authorization code
4. The backend exchanges the code for access tokens
5. The frontend can use the access token to make authenticated requests

## Protected Endpoints

- `GET /users/me`: Get current user information (requires authentication)
