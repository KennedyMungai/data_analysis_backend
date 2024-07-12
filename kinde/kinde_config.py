"""The file containing the Kinde configuration"""
import os

from dotenv import find_dotenv, load_dotenv
from kinde_sdk import Configuration
from kinde_sdk.kinde_api_client import GrantType, KindeApiClient

load_dotenv(find_dotenv())

CONFIG_DOMAIN = os.environ.get('KINDE_ISSUER_URL')
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
CALLBACK_URL = os.environ.get('KINDE_CALLBACK_URL')


configuration = Configuration(host=CONFIG_DOMAIN)
kinde_api_client_params = {
    "configuration": configuration,
    "domain": CONFIG_DOMAIN,
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "grant_type": GrantType.AUTHORIZATION_CODE,
    "callback_url": CALLBACK_URL
}
kinde_client = KindeApiClient(**kinde_api_client_params)
