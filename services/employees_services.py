"""The file containing the employee services"""
from typing import List
from uuid import UUID

from fastapi import Depends
from sqlalchemy.orm import Session

from database.db import get_db
from models.models import Employees
from schemas.employees_schema import (CreateEmployee, ReadEmployee,
                                      UpdateEmployee)


async def retrieve_all_the_employees_in_a_region_service(
    _region_id: UUID, _db: Session = Depends(get_db)
) -> List[ReadEmployee]:
    """The service used to fetch all employees from the database

    Args:
        _region_id (UUID): The id of the region
        _db (Session): The database session

    Returns:
        List[ReadEmployee]: A list of the employees fetched
    """
    return _db.query(Employees).filter(Employees.region_id == _region_id).all()


async def retrieve_all_the_employees_in_a_store_service(
    _store_id: UUID,
    _db: Session = Depends(get_db)
) -> List[ReadEmployee]:
    """The service function to retrieve the employee info of all the employees in a store`

    Args:
        _store_id (UUID): The id of the store
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        List[ReadEmployee]: A list of the employees
    """
    return _db.query(Employees).filter(Employees.store_id == _store_id).all()


async def retrieve_all_the_employees_service(
    _db: Session = Depends(get_db)
) -> List[ReadEmployee]:
    """The service function to retrieve all the employees

    Args:
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        List[ReadEmployee]: A list of the employees
    """
    return _db.query(Employees).all()


async def retrieve_one_employee_service(
    _employee_id: UUID,
    _db: Session = Depends(get_db)
) -> ReadEmployee:
    """The service function to retrieve a specific employee from the database

    Args:
        _employee_id (UUID): The id of the employee
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        ReadEmployee: The retrieved employee data
    """
    return _db.query(Employees).filter(Employees.employee_id == _employee_id).first()


async def create_employee_service(
    _employee_data: CreateEmployee,
    _db: Session = Depends(get_db)
) -> ReadEmployee:
    """The service function for creating employees in the database

    Args:
        _employee_data (CreateEmployee): The schema for creating employees
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        ReadEmployee: The newly created employee
    """
    employee = Employees(**_employee_data.model_dump())
    _db.add(employee)
    _db.commit()
    _db.refresh(employee)
    return employee


async def update_employee_service(
    _employee_id: UUID,
    _update_employee_data: UpdateEmployee,
    _db: Session = Depends(get_db)
) -> ReadEmployee:
    """The service function for updating employees in the database

    Args:
        _employee_id (UUID): The id of the employee in the database
        _update_employee_data (UpdateEmployee): The schema for updating employees
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        ReadEmployee: The newly update employee info
    """
    _db.query(Employees).filter(Employees.employee_id == _employee_id).update(
        _update_employee_data.model_dump())
    _db.commit()
    return _db.query(Employees).filter(Employees.employee_id == _employee_id).first()


async def delete_employee_service(
    _employee_id: UUID,
    _db: Session = Depends(get_db)
) -> None:
    """The service function for deleting employees in the database

    Args:
        _employee_id (UUID): The id of the employee in the database
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        None
    """
    employee = await retrieve_one_employee_service(_employee_id, _db)

    if not employee:
        return

    _db.delete(employee)
    _db.commit()
