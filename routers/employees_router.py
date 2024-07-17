"""The employees router file"""
from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.db import get_db
from schemas.employees_schema import (CreateEmployee, ReadEmployee,
                                      UpdateEmployee)
from services.employees_services import (
    create_employee_service, delete_employee_service,
    retrieve_all_the_employees_in_a_region_service,
    retrieve_all_the_employees_in_a_store_service,
    retrieve_all_the_employees_service, retrieve_one_employee_service,
    update_employee_service)

employees_router = APIRouter(prefix='/employees', tags=['Employees'])


@employees_router.get(
    '/',
    description='Retrieves all employees',
    status_code=status.HTTP_200_OK
)
async def retrieve_all_the_employees_endpoint(_db: Session = Depends(get_db)) -> List[ReadEmployee]:
    """The endpoint function to retrieve all the employees

    Args:
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        List[ReadEmployee]: A list of the employees
    """
    try:
        return await retrieve_all_the_employees_service(_db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e


@employees_router.get(
    '/region/{_region_id}',
    description='Retrieves all employees in a region',
    status_code=status.HTTP_200_OK
)
async def retrieve_all_the_employees_in_a_region_endpoint(
    _region_id: UUID,
    _db: Session = Depends(get_db)
) -> List[ReadEmployee]:
    """The endpoint function to retrieve all the employees in a region

    Args:
        _region_id (UUID): The id of the region
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        List[ReadEmployee]: A list of the employees
    """
    try:
        return await retrieve_all_the_employees_in_a_region_service(
            _region_id, _db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e


@employees_router.get(
    '/store/{_store_id}',
    description='Retrieves all employees in a store',
    status_code=status.HTTP_200_OK
)
async def retrieve_all_the_employees_in_a_store_endpoint(
    _store_id: UUID,
    _db: Session = Depends(get_db)
) -> List[ReadEmployee]:
    """The endpoint function to retrieve all the employees in a store

    Args:
        _store_id (UUID): The id of the store
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        List[ReadEmployee]: A list of the employees
    """
    try:
        return await retrieve_all_the_employees_in_a_store_service(
            _store_id, _db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e


@employees_router.get(
    '/{_employee_id}',
    description='Retrieves one employee',
    status_code=status.HTTP_200_OK
)
async def retrieve_one_employee_endpoint(
    _employee_id: UUID,
    _db: Session = Depends(get_db)
) -> ReadEmployee:
    """The endpoint function to retrieve a specific employee

    Args:
        employee_id (UUID): The id of the employee
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        ReadEmployee: The employee
    """
    try:
        return await retrieve_one_employee_service(_employee_id, _db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e


@employees_router.post(
    '/',
    description='Creates a new employee',
    status_code=status.HTTP_201_CREATED
)
async def create_employee_endpoint(
    _employee_data: CreateEmployee,
    _db: Session = Depends(get_db)
) -> ReadEmployee:
    """The endpoint function to create a new employee

    Args:
        _employee_data (CreateEmployee): The schema for creating an employee
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        ReadEmployee: The newly created employee
    """
    try:
        return await create_employee_service(_employee_data, _db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e


@employees_router.put(
    '/{_employee_id}',
    description='Updates an employee',
    status_code=status.HTTP_202_ACCEPTED
)
async def update_employee_endpoint(
    _employee_id: UUID,
    _employee_data: UpdateEmployee,
    _db: Session = Depends(get_db)
) -> ReadEmployee:
    """The endpoint function to update an employee

    Args:
        employee_id (UUID): The id of the employee
        _employee_data (UpdateEmployee): The data used to update an employee
        _db (Session, optional): The database session. Defaults to Depends(get_db). 

    Returns:
        ReadEmployee: The updated employee
    """
    try:
        return await update_employee_service(_employee_id, _employee_data, _db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e


@employees_router.delete(
    '/{_employee_id}',
    description='Deletes an employee',
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_employee_endpoint(
    _employee_id: UUID,
    _db: Session = Depends(get_db)
) -> None:
    """The endpoint function to delete an employee

    Args:
        employee_id (UUID): The id of the employee
        _db (Session, optional): The database session. Defaults to Depends(get_db).
    """
    try:
        return await delete_employee_service(_employee_id, _db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e
