"""The router containing the authentication endpoints"""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from utils.password_hashing import verify_password
from database.db import get_db
from models.models import Employees

auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post(
    "/login",
    response_model=dict,
    name="login",
    status_code=status.HTTP_200_OK
)
async def login(
    _user_credentials: OAuth2PasswordRequestForm = Depends(),
    _db: Session = Depends(get_db)
):
    """The endpoint used for logging in users

    Args:
        _user_credentials (OAuth2PasswordRequestForm, optional): The user credentials. 
            Defaults to Depends().
        _db (Session, optional): The db session. Defaults to Depends(get_db).
    """
    user = _db.query(Employees).filter(
        Employees.employee_email == _user_credentials.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")

    if not verify_password(_user_credentials.password, user.employee_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")

    # Create and return an access token
