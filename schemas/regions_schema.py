"""The schema file for regions"""
from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from schemas.employees_schema import ReadEmployee
from schemas.incidents_schema import ReadIncident
from schemas.stores_schema import ReadStore


class RegionBase(BaseModel):
    """The base schema for the regions data

    Args:
        BaseModel (Pydantic): The base class for the models
    """
    region_name: str


class CreateRegion(RegionBase):
    """The schema used for creating regions

    Args:
        RegionBase (BaseModel): The base schema for the regions data
    """


class ReadRegion(RegionBase):
    """The schema used for reading regions

    Args:
        RegionBase (BaseModel): The base schema for the regions data
    """
    region_id: UUID
    created_at: datetime
    updated_at: Optional[datetime] = None

    stores: List[ReadStore]
    employees: List[ReadEmployee]
    incidents: List[ReadIncident]

    class Config:
        """Config subclass for reading region data"""
        from_attributes = True


class UpdateRegion(BaseModel):
    """The schema used to update region data

    Args:
        BaseModel (Pydantic): The base class for all schemas
    """
    region_name: Optional[str] = None

    class Config:
        """The config subclass for reading data"""
        from_attributes = True
