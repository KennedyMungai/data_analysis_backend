"""The main file for the API"""
import os

from dotenv import find_dotenv, load_dotenv
from fastapi import FastAPI, status
from starlette.middleware.sessions import SessionMiddleware

from routers.employees_router import employees_router
from routers.incidents_router import incidents_router
from routers.regions_router import regions_router
from routers.store_sections_router import store_sections_router
from routers.stores_router import stores_router

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
async def root():
    """The root endpoint of the application

    Returns:
        dict: A simple message
    """
    return {'Message': 'Hello World'}


app.include_router(regions_router)
app.include_router(stores_router)
app.include_router(employees_router)
app.include_router(store_sections_router)
app.include_router(incidents_router)
