"""The router for the stores"""
from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.db import get_db
from schemas.stores_schema import ReadStore, CreateStore, UpdateStore
from services.stores_services import (create_store_service,
                                      delete_store_service,
                                      retrieve_all_stores_in_a_region_service,
                                      retrieve_one_store_service,
                                      update_store_service)

stores_router = APIRouter(prefix='/stores', tags=['Stores'])


@stores_router.get('/', description='Retrieves all stores', status_code=status.HTTP_200_OK)
async def retrieve_all_stores_in_a_region_endpoint(
    _region_id: UUID, _db: Session = Depends(get_db)
) -> List[ReadStore]:
    """The endpoint to show all stores in a region

    Args:
        _region_id (UUID): The id of a region
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        List[ReadStore]: A list of the stores
    """
    try:
        return await retrieve_all_stores_in_a_region_service(
            _region_id, _db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e


@stores_router.get(
    "/{_store_id}",
    description="Retrieves one store",
    status_code=status.HTTP_200_OK
)
async def retrieve_one_store_endpoint(_store_id: UUID, _db: Session = Depends(get_db)) -> ReadStore:
    """The endpoint to show a specific store

    Args:
        store_id (UUID): The id of a store
        db (Session): The database session

    Returns:
        ReadStore: The store
    """
    try:
        return await retrieve_one_store_service(_store_id, _db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e


@stores_router.post('/', description='Creates a store', status_code=status.HTTP_201_CREATED)
async def create_store_endpoint(
    _region_id: UUID,
    _store_data: CreateStore,
    _db: Session = Depends(get_db)
) -> ReadStore:
    """The endpoint to create a store

    Args:
        _region_id (UUID): The region id
        _store_data (CreateStore): The store data
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        ReadStore: The newly created store
    """
    try:
        return await create_store_service(_store_data, _region_id, _db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e


@stores_router.put(
    "/{store_id}",
    description="Updates a store",
    status_code=status.HTTP_202_ACCEPTED
)
async def update_store_endpoint(
    _store_id: UUID,
    _store_data: UpdateStore,
    _db: Session = Depends(get_db)
) -> ReadStore:
    """The endpoint to update a store

    Args:
        store_id (UUID): The id of the store
        store_data (UpdateStore): The store data
        db (Session): The database session

    Returns:
        ReadStore: The updated store
    """
    try:
        return await update_store_service(_store_id, _store_data, _db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        ) from e


@stores_router.delete(
    "/{_store_id}",
    description="Deletes a store",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_store_endpoint(_store_id: UUID, _db: Session = Depends(get_db)) -> None:
    """The endpoint to delete a store

    Args:
        store_id (UUID): The id of the store
        db (Session): The database session
    """
    try:
        await delete_store_service(_store_id, _db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e
