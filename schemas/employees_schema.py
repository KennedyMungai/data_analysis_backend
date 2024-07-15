"""The file containing the schemas for the employees"""
from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr


class EmployeeBase(BaseModel):
    """The base schema for the employees model

    Args:
        BaseModel (Pydantic): The base model for the employees
    """
    employee_name: str
    employee_email: EmailStr
    employee_phone_number: str


class ReadEmployee(EmployeeBase):
    """The schema used for reading employee data

    Args:
        EmployeeBase (Pydantic): The base schema for the employees
    """
    employee_id: UUID
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        """Config subclass for reading employee data"""
        from_attributes = True


class CreateEmployee(EmployeeBase):
    """The schema used to create employees

    Args:
        EmployeeBase (Pydantic): The base schema for the employees
    """


class UpdateEmployee(BaseModel):
    """Yhe schema used to update employees

    Args:
        BaseModel (Pydantic): The base model for all schemas
    """
    employee_name: Optional[str] = None
    employee_email: Optional[EmailStr] = None
    employee_phone_number: Optional[str] = None

    class Config:
        """The config subclass for reading data"""
        from_attributes = True
