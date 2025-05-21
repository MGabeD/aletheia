import os
from dotenv import load_dotenv
from httpx_oauth.clients.google import GoogleOAuth2
from aletheia.utils import get_postgres_url

load_dotenv()


DATABASE_URL = get_postgres_url()
SECRET = os.getenv("USER_MANAGER_SECRET")
GOOGLE_OAUTH_CLIENT_ID = os.getenv("GOOGLE_OAUTH_CLIENT_ID")
GOOGLE_OAUTH_CLIENT_SECRET = os.getenv("GOOGLE_OAUTH_CLIENT_SECRET")
GOOGLE_OAUTH_REDIRECT_URI = os.getenv("GOOGLE_OAUTH_REDIRECT_URI")

google_oauth_client = GoogleOAuth2(
    GOOGLE_OAUTH_CLIENT_ID,
    GOOGLE_OAUTH_CLIENT_SECRET,
)

