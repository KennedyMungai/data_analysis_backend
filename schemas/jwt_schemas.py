"""The schemas for the JWT data"""
from typing import Optional

from pydantic import BaseModel


class EmployeeLogin(BaseModel):
    """The schema used when an employee is trying to log in

    Args:
        BaseModel (Pydantic): The base class for all schemas
    """
    employee_email: str
    employee_password: str


class EmployeeToken(BaseModel):
    """The schema used when an employee is trying to log in

    Args:
        BaseModel (Pydantic): The base class for all schemas
    """
    access_token: str
    token_type: str


class EmployeeTokenData(BaseModel):
    """The schema used when an employee is trying to log in

    Args:
        BaseModel (Pydantic): The base class for all schemas
    """
    id: Optional[str] = None

    class Config:
        """The subclass for reading data from the database"""
        orm_mode = True
