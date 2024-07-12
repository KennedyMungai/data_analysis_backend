"""The file that stores the Kind authentication logic"""
from fastapi import HTTPException, Request, status
from kinde_sdk.kinde_api_client import KindeApiClient

from kinde.kinde_config import kinde_api_client_params

user_clients = {}


def get_kinde_client(request: Request) -> KindeApiClient:
    """The function that handles endpoint security

    Args:
        request (Request): The request for info

    Returns:
        KindeApiClient: The KindeApiClient instance
    """
    user_id = request.session.get('user_id')

    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized")

    if user_id not in user_clients:
        user_clients[user_id] = KindeApiClient(**kinde_api_client_params)

    kinde_client = user_clients[user_id]

    if not kinde_client.is_authenticated():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='Not Authorized!')

    return kinde_client
