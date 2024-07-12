"""The main file for the API"""
from fastapi import FastAPI, status

app = FastAPI(title='Data Analysis',
              description='The backend for a data analysis application',
              version='0.1.0'
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
