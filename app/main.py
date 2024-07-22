"""The main file for the API"""
import os

from dotenv import find_dotenv, load_dotenv
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
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

origins = ['http://localhost:3000',
           'https://data-analysis-frontend.vercel.app/']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


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
app.include_router(store_sections_router)
app.include_router(incidents_router)
