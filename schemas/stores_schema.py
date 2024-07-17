"""The file that holds the store schemas"""
from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from schemas.employees_schema import ReadEmployee
from schemas.incidents_schema import ReadIncident
from schemas.store_sections_schema import ReadStoreSection


class StoreBase(BaseModel):
    """The base model of all stores

    Args:
        BaseModel (Pydantic): The base class for all schemas
    """
    store_name: str


class ReadStore(StoreBase):
    """The schema used for reading store data

    Args:
        StoreBase (Pydantic): The base model of all stores
    """
    store_id: UUID
    created_at: datetime
    updated_at: Optional[datetime] = None

    employees: List[ReadEmployee]
    incidents: List[ReadIncident]
    store_sections: List[ReadStoreSection]

    class Config:
        """Config subclass for reading store data"""
        from_attributes = True


class CreateStore(StoreBase):
    """The schema used to create stores

    Args:
        StoreBase (Pydantic): The base model of all stores
    """
    region_id: UUID


class UpdateStore(BaseModel):
    """The schema used to update store data

    Args:
        BaseModel (Pydantic): The base for all schemas
    """
    store_name: Optional[str] = None

    class Config:
        """The config subclass for reading data"""
        from_attributes = True
