"""The schema file for incidents in the store"""
from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class IncidentsBase(BaseModel):
    """The base schema for the incidents

    Args:
        BaseModel (Pydantic): The base class for all schemas
    """
    incident_description: str
    product_name: str
    product_code: str
    product_quantity: int
    product_price: float
    employee_name: str
    employee_email: str


class CreateIncident(IncidentsBase):
    """The schema used to create an incident

    Args:
        IncidentsBase (Pydantic): The base class for the schema
    """
    region_id: UUID
    store_id: UUID
    store_section_id: UUID
    employee_id: str


class ReadIncident(IncidentsBase):
    """The schema used to read an incident

    Args:
        IncidentsBase (Pydantic): The base class for the schema
    """
    incident_id: UUID
    region_id: UUID
    store_id: UUID
    store_section_id: UUID
    employee_id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        """The subclass for reading data from the database"""
        from_attributes = True


class UpdateIncident(BaseModel):
    """The schema used to update incidents

    Args:
        BaseModel (Pydantic): The base class for all schemas
    """

    incident_description: Optional[str]
    product_name: Optional[str]
    product_code: Optional[str]
    product_quantity: Optional[int]
    product_price: Optional[float]

    class Config:
        """The subclass for reading data from the database"""
        from_attributes = True
