from fastapi import APIRouter
from aletheia.backend.core.settings import google_oauth_client, SECRET
from aletheia.backend.schemas.users import UserCreate, UserRead, UserUpdate
from aletheia.backend.core.auth import auth_backend, fastapi_users


router = APIRouter(prefix="/auth", tags=["auth"])


# JWT login and logout
router.include_router(
    fastapi_users.get_auth_router(auth_backend), 
    prefix="/jwt", 
    tags=["auth"]
)

# Register and verify   
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate), 
    prefix="/register", 
    tags=["auth"]
)
# Straight copied from the docs - does not do anything yet. Will need to implement sending email verification.
# If I want this 
router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="",
    tags=["auth"],
)

# Password reset
router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="",
    tags=["auth"],
)

# # get/update user router
# router.include_router(
#     fastapi_users.get_users_router(UserRead, UserUpdate),
#     prefix="/users",
#     tags=["users"],
# )

# Google OAuth
router.include_router(
    fastapi_users.get_oauth_router(google_oauth_client, auth_backend, SECRET),
    prefix="/google",
    tags=["auth"],
)