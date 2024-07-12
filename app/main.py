"""The main file for the API"""
import os

from dotenv import find_dotenv, load_dotenv
from fastapi import Depends, FastAPI, status
from kinde_sdk.kinde_api_client import KindeApiClient
from starlette.middleware.sessions import SessionMiddleware

from kinde.kinde import get_kinde_client

load_dotenv(find_dotenv())

SECRET_KEY = os.environ.get('SECRET_KEY')

app = FastAPI(title='Data Analysis',
              description='The backend for a data analysis application',
              version='0.1.0'
              )

app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)


@app.get(
    '/',
    tags=['Root'],
    description='The root endpoint of the application',
    status_code=status.HTTP_200_OK
)
async def root(kinde_client: KindeApiClient = Depends(get_kinde_client)):
    """The root endpoint of the application

    Returns:
        dict: A simple message
    """
    print(kinde_client)
    return {'Message': 'Hello World'}
