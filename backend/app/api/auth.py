"""
Authentication API endpoints using Supabase Auth
"""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime
from app.models.schemas import UserCreate, UserLogin, UserResponse, Token
from app.config import settings
from app.database import get_db
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/auth", tags=["Authentication"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate, db=Depends(get_db)):
    """
    Register a new user using Supabase Auth.
    
    Args:
        user: UserCreate schema with email and password
        db: Database client
        
    Returns:
        UserResponse with user details
    """
    try:
        # Use Supabase Auth to create user
        auth_response = db.auth.sign_up({
            "email": user.email,
            "password": user.password,
            "options": {
                "data": {
                    "full_name": user.full_name
                }
            }
        })
        
        if auth_response.user is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Registration failed. Email may already be in use."
            )
        
        return UserResponse(
            id=auth_response.user.id,
            email=auth_response.user.email,
            full_name=user.full_name,
            created_at=datetime.fromisoformat(auth_response.user.created_at)
        )
        
    except Exception as e:
        logger.error(f"Registration error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Registration failed: {str(e)}"
        )


@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db=Depends(get_db)):
    """
    Login using Supabase Auth.
    
    Args:
        form_data: OAuth2 form with username (email) and password
        db: Database client
        
    Returns:
        Token with access_token
    """
    try:
        # Use Supabase Auth to sign in
        auth_response = db.auth.sign_in_with_password({
            "email": form_data.username,
            "password": form_data.password
        })
        
        if auth_response.session is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password"
            )
        
        return Token(access_token=auth_response.session.access_token)
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Login error: {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )


async def get_current_user(token: str = Depends(oauth2_scheme), db=Depends(get_db)) -> dict:
    """
    Get current user from Supabase Auth token.
    
    Args:
        token: JWT access token from Supabase
        db: Database client
        
    Returns:
        User data dict
    """
    try:
        # Verify token with Supabase
        user_response = db.auth.get_user(token)
        
        if user_response.user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        
        return {
            "id": user_response.user.id,
            "email": user_response.user.email,
            "full_name": user_response.user.user_metadata.get("full_name"),
            "created_at": user_response.user.created_at
        }
        
    except Exception as e:
        logger.error(f"Auth error: {e}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.get("/me", response_model=UserResponse)
async def get_me(current_user: dict = Depends(get_current_user)):
    """Get current user profile."""
    return UserResponse(
        id=current_user["id"],
        email=current_user["email"],
        full_name=current_user.get("full_name"),
        created_at=datetime.fromisoformat(current_user["created_at"])
    )
