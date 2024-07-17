"""The router file for the incidents CRUD operations"""
from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.db import get_db
from schemas.incidents_schema import (CreateIncident, ReadIncident,
                                      UpdateIncident)
from services.incidents_services import (
    create_incident_service, delete_an_incident_service,
    retrieve_a_single_incident_service,
    retrieve_all_incidents_in_a_region_service,
    retrieve_all_incidents_in_a_store_section_service,
    retrieve_all_incidents_in_a_store_service,
    retrieve_all_incidents_reported_by_an_employee_service,
    update_an_incident_service)

incidents_router = APIRouter(prefix="/incidents", tags=["Incidents"])


@incidents_router.post(
    '/',
    name="Create An Incident",
    response_model=ReadIncident,
    status_code=status.HTTP_201_CREATED
)
async def create_incident_endpoint(
    _incident_data: CreateIncident,
    _db: Session = Depends(get_db)
) -> ReadIncident:
    """The endpoint for creating incidents

    Args:
        incident_data (CreateIncident): The incident data
        db (Session): The database session

    Returns:
        ReadIncident: The incident data
    """
    try:
        return await create_incident_service(_incident_data, _db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(e)) from e


@incidents_router.get(
    '/region/{_region_id}',
    response_model=ReadIncident,
    name="Retrieve A Single Incident",
    status_code=status.HTTP_200_OK
)
async def retrieve_all_incidents_in_a_region_endpoint(
    _region_id: UUID,
    _db: Session = Depends(get_db)
) -> ReadIncident:
    """The endpoint for reading incidents

    Args:
        incident_id (str): The incident id
        db (Session): The database session

    Returns:
        ReadIncident: The incident data
    """
    try:
        return await retrieve_all_incidents_in_a_region_service(_region_id, _db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(e)) from e


@incidents_router.get(
    '/store/{_store_id}',
    response_model=List[ReadIncident],
    name="Retrieve all incidents in a store",
    status_code=status.HTTP_200_OK
)
async def retrieve_all_incidents_in_a_store_endpoint(
    _store_id: UUID,
    _db: Session = Depends(get_db)
) -> List[ReadIncident]:
    """The endpoint for reading incidents

    Args:
        store_id (str): The store id
        db (Session): The database session

    Returns:
        List[ReadIncident]: The incident data
    """
    try:
        return await retrieve_all_incidents_in_a_store_service(_store_id, _db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(e)) from e


@incidents_router.get(
    '/store_section/{_store_section_id}',
    response_model=List[ReadIncident],
    name="Retrieve all incidents in a store section",
    status_code=status.HTTP_200_OK
)
async def retrieve_all_incidents_in_a_store_section_endpoint(
    _store_section_id: UUID,
    _db: Session = Depends(get_db)
) -> List[ReadIncident]:
    """The endpoint for reading incidents

    Args:
        store_section_id (str): The store section id
        db (Session): The database session

    Returns:
        List[ReadIncident]: The incident data
    """
    try:
        return await retrieve_all_incidents_in_a_store_section_service(
            _store_section_id, _db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(e)) from e


@incidents_router.get(
    '/employee/{_employee_id}',
    response_model=List[ReadIncident],
    name="Retrieve all incidents reported by an employee",
    status_code=status.HTTP_200_OK
)
async def retrieve_all_incidents_reported_by_an_employee_endpoint(
    _employee_id: UUID,
    _db: Session = Depends(get_db)
) -> List[ReadIncident]:
    """The endpoint for reading incidents

    Args:
        employee_id (str): The employee id
        db (Session): The database session

    Returns:
        List[ReadIncident]: The incident data
    """
    try:
        return await retrieve_all_incidents_reported_by_an_employee_service(
            _employee_id, _db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(e)) from e


@incidents_router.get(
    '/{_incident_id}',
    response_model=List[ReadIncident],
    name="Retrieve an incident",
    status_code=status.HTTP_200_OK
)
async def retrieve_an_incident_endpoint(
    _incident_id: UUID,
    _db: Session = Depends(get_db)
) -> List[ReadIncident]:
    """The endpoint for reading incidents

    Args:
        incident_id (str): The incident id
        db (Session): The database session

    Returns:
        List[ReadIncident]: The incident data
    """
    try:
        return await retrieve_a_single_incident_service(_incident_id, _db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=str(e)) from e


@incidents_router.put(
    '/{_incident_id}',
    response_model=ReadIncident,
    name="Update an incident",
    status_code=status.HTTP_202_ACCEPTED
)
async def update_an_incident_endpoint(
    _incident_id: UUID,
    incident: UpdateIncident,
    _db: Session = Depends(get_db)
) -> ReadIncident:
    """The endpoint for updating incidents

    Args:
        incident_id (str): The incident id
        incident (UpdateIncident): The incident data
        db (Session): The database session

    Returns:
        ReadIncident: The incident data
    """
    try:
        return await update_an_incident_service(_incident_id, incident, _db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(e)) from e


@incidents_router.delete(
    '/{_incident_id}',
    name="Delete an incident",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_an_incident_endpoint(
    _incident_id: UUID,
    _db: Session = Depends(get_db)
) -> None:
    """The endpoint for deleting incidents

    Args:
        incident_id (str): The incident id
        db (Session): The database session
    """
    try:
        return await delete_an_incident_service(_incident_id, _db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(e)) from e
