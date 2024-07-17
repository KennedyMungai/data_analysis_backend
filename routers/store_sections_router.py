"""The router file for the store sections CRUD operations"""
from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.db import get_db
from schemas.store_sections_schema import (CreateStoreSection,
                                           ReadStoreSection,
                                           UpdateStoreSection)
from services.store_sections_services import (
    create_store_section_service, delete_store_section_service,
    retrieve_all_store_sections_from_a_store_service,
    retrieve_single_store_section_service, update_store_section_service)

store_sections_router = APIRouter(
    prefix='/store_sections', tags=['Store Sections'])


@store_sections_router.post(
    '/',
    response_model=ReadStoreSection,
    name="create_store_section",
    status_code=status.HTTP_201_CREATED
)
async def create_store_section_endpoint(
        _store_section: CreateStoreSection,
        _db: Session = Depends(get_db)
) -> ReadStoreSection:
    """The endpoint for creating store sections

    Args:
        store_section (CreateStoreSection): The store section data
        db (Session): The database session

    Returns:
        ReadStoreSection: The store section data
    """
    try:
        return await create_store_section_service(_store_section, _db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(e)) from e


@store_sections_router.get(
    '/{_store_section_id}',
    response_model=ReadStoreSection,
    name="retrieve_single_store_section",
    status_code=status.HTTP_200_OK
)
async def retrieve_single_store_section_endpoint(
        _store_section_id: UUID,
        _db: Session = Depends(get_db)
) -> ReadStoreSection:
    """The endpoint for reading store sections

    Args:
        store_section_id (str): The store section id
        db (Session): The database session

    Returns:
        ReadStoreSection: The store section data
    """
    try:
        return await retrieve_single_store_section_service(_store_section_id, _db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=str(e)) from e


@store_sections_router.get(
    '/{_store_id}',
    response_model=List[ReadStoreSection],
    name="retrieve_all_store_sections_in_a_store",
    status_code=status.HTTP_200_OK
)
async def retrieve_all_store_sections_in_a_store_endpoint(
        _store_id: UUID,
        _db: Session = Depends(get_db)
) -> List[ReadStoreSection]:
    """The endpoint for updating store sections

    Args:
        _store_id (str): The store id
        db (Session): The database session

    Returns:
        List[ReadStoreSection]: The list of store section data
    """
    try:
        return await retrieve_all_store_sections_from_a_store_service(_store_id, _db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(e)) from e


@store_sections_router.put(
    '/{_store_section_id}',
    response_model=ReadStoreSection,
    name="update_store_section",
    status_code=status.HTTP_202_ACCEPTED
)
async def update_store_section_endpoint(
        _store_section_id: UUID,
        _store_section: UpdateStoreSection,
        _db: Session = Depends(get_db)
) -> ReadStoreSection:
    """The endpoint for updating store sections

    Args:
        store_section_id (str): The store section id
        store_section (UpdateStoreSection): The store section data
        db (Session): The database session

    Returns:
        ReadStoreSection: The store section data
    """
    try:
        return await update_store_section_service(_store_section_id, _store_section, _db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(e)) from e


@store_sections_router.delete(
    '/{_store_section_id}',
    name="delete_store_section",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_store_section_endpoint(
        _store_section_id: UUID,
        _db: Session = Depends(get_db)
) -> None:
    """The endpoint for deleting store sections

    Args:
        store_section_id (str): The store section id
        db (Session): The database session

    Returns:
        None
    """
    try:
        return await delete_store_section_service(_store_section_id, _db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=str(e)) from e
