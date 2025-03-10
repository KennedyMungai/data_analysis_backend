"""The schema file for the store sections"""
from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from schemas.incidents_schema import ReadIncident


class StoreSectionsBase(BaseModel):
    """The base model for the store sections data

    Args:
        BaseModel (Pydantic): The base class for all schemas
    """
    store_section_name: str


class ReadStoreSection(StoreSectionsBase):
    """The schema used to read the store section data

    Args:
        StoreSectionsBase (Pydantic): The base class for the schema
    """
    store_section_id: UUID
    created_at: datetime
    updated_at: Optional[datetime]

    incidents: List[ReadIncident]

    class Config:
        """A subclass for reading data from the database"""
        from_attributes = True


class CreateStoreSection(StoreSectionsBase):
    """The schema used to create the store section

    Args:
        StoreSectionsBase (Pydantic): The base class for the schema
    """
    store_id: UUID


class UpdateStoreSection(BaseModel):
    """The schema used to update the store section

    Args:
        BaseModel (Pydantic): The base class for all schemas
    """
    store_section_name: Optional[str] = None

    class Config:
        """The config file for reading data from the database"""
        from_attributes = True
