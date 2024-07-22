"""The file containing the service functions for the incidents data"""
from typing import List
from uuid import UUID

from sqlalchemy.orm import Session

from models.models import Incidents
from schemas.incidents_schema import (CreateIncident, ReadIncident,
                                      UpdateIncident)


async def create_incident_service(
        _incident_data: CreateIncident, _db: Session) -> ReadIncident:
    """The service function for creating incidents in the database

    Args:
        _incident_data (CreateIncident): The incident data
        _db (Session): The database session

    Returns:
        ReadIncident: The newly created incident
    """
    incident = Incidents(**_incident_data.model_dump())
    _db.add(incident)
    _db.commit()
    _db.refresh(incident)
    return incident


async def retrieve_all_incidents_in_a_region_service(
    _region_id: UUID,
    _db: Session
) -> List[ReadIncident]:
    """The service used to fetch all incidents from the database

    Args:
        _db (Session): The database session

    Returns:
        List[ReadIncident]: A list of the incidents fetched
    """
    return _db.query(Incidents).filter(Incidents.region_id == _region_id).all()


async def retrieve_all_incidents_in_a_store_service(
    _store_id: UUID,
    _db: Session
) -> List[ReadIncident]:
    """The service used to fetch all incidents from the database

    Args:
        _db (Session): The database session

    Returns:
        List[ReadIncident]: A list of the incidents fetched
    """
    return _db.query(Incidents).filter(Incidents.store_id == _store_id).all()


async def retrieve_all_incidents_in_a_store_section_service(
    _store_section_id: UUID,
    _db: Session
) -> List[ReadIncident]:
    """The service used to fetch all incidents from the database

    Args:
        _db (Session): The database session

    Returns:
        List[ReadIncident]: A list of the incidents fetched
    """
    return _db.query(Incidents).filter(Incidents.store_section_id == _store_section_id).all()


async def retrieve_all_incidents_reported_by_an_employee_service(
    _employee_id: str,
    _db: Session
) -> List[ReadIncident]:
    """The service used to fetch all incidents from the database

    Args:
        _db (Session): The database session

    Returns:
        List[ReadIncident]: A list of the incidents fetched
    """
    return _db.query(Incidents).filter(Incidents.employee_id == _employee_id).all()


async def retrieve_a_single_incident_service(
        _incident_id: UUID,
        _db: Session) -> ReadIncident:
    """The service function to retrieve a single incident

    Args:
        _incident_id (UUID): The id of the incident
        _db (Session): The database session

    Returns:
        ReadIncident: The retrieved incident
    """
    return _db.query(Incidents).filter(Incidents.incident_id == _incident_id).first()


async def update_an_incident_service(
        _incident_id: UUID,
        _update_incident_data: UpdateIncident,
        _db: Session) -> ReadIncident:
    """The service function for updating incidents in the database

    Args:
        _incident_id (UUID): The id of the incident in the database
        _update_incident_data (UpdateIncident): The schema for updating incidents
        _db (Session): The database session

    Returns:
        ReadIncident: The updated incident
    """
    _db.query(Incidents).filter(Incidents.incident_id == _incident_id).update(
        _update_incident_data.model_dump())

    _db.commit()
    return await retrieve_a_single_incident_service(_incident_id, _db)


async def delete_an_incident_service(
        _incident_id: UUID,
        _db: Session) -> None:
    """The service function for deleting incidents in the database

    Args:
        _incident_id (UUID): The id of the incident in the database
        _db (Session): The database session
    """
    _db.query(Incidents).filter(Incidents.incident_id == _incident_id).delete()
    _db.commit()
