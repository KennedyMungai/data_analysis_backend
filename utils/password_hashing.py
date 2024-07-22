"""The file containing the password hashing and verification functions"""
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(_password: str) -> str:
    """The function used to hash passwords

    Args:
        _password (str): The password

    Returns:
        str: The hashed string password
    """
    return pwd_context.hash(_password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """The function used to verify the password against the hashed password in the database

    Args:
        plain_password (str): The plain password
        hashed_password (str): The hashed password

    Returns:
        bool: A boolean value indicating whether the two password hashes are a match
    """
    return pwd_context.verify(plain_password, hashed_password)
