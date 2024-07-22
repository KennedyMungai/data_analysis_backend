"""The file containing the OAuth2 JWT shenanigans"""
import os
from datetime import datetime, timedelta

from dotenv import find_dotenv, load_dotenv
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from database.db import get_db
from schemas.jwt_schemas import EmployeeTokenData
from services.employees_services import retrieve_one_employee_service

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

load_dotenv(find_dotenv())

SECRET_KEY = os.environ.get('SECRET_KEY')
ALGORITHM = os.environ.get('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES')


async def create_access_token(data: dict):
    """the function that creates the access tokens

    Args:
        data (dict): The data to be encoded
    """
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})

    encoded_jwt = await jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return await encoded_jwt


async def verify_access_token(_token: str, _credentials_exception):
    """The function that verifies access tokens

    Args:
        _token (str): The token
        _credentials_exception (_type_): The exception

    Raises:
        _credentials_exception: _description_
        _credentials_exception: _description_

    Returns:
        _type_: _description_
    """
    try:
        payload = jwt.decode(_token, SECRET_KEY, algorithms=[ALGORITHM])
        _id: str = payload.get("employee_id")

        if _id is None:
            raise _credentials_exception
        token_data = EmployeeTokenData(id=_id)
    except JWTError as e:
        raise _credentials_exception from e

    return token_data


async def get_current_user(
    _token: str = Depends(oauth2_scheme),
    _db: Session = Depends(get_db)
):
    """The function to retrieve the currently logged in user

    Args:
        _token (str, optional): _description_. Defaults to Depends(oauth2_scheme).
        _db (Session, optional): _description_. Defaults to Depends(get_db).

    Returns:
        _type_: _description_
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'}
    )

    token = await verify_access_token(_token, credentials_exception)

    employee = await retrieve_one_employee_service(token.id, _db)

    return employee
