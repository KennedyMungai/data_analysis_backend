"""The routing file for the regions data"""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.db import get_db
from schemas.regions_schema import CreateRegion, ReadRegion, UpdateRegion
from services.regions_service import (create_region_service,
                                      delete_region_service,
                                      retrieve_all_regions_service,
                                      retrieve_one_region_service,
                                      update_region_service)

regions_router = APIRouter(prefix='/regions', tags=['Regions'])


@regions_router.get('/', description='Retrieves all regions', status_code=status.HTTP_200_OK)
async def retrieve_all_regions_endpoint(_db: Session = Depends(get_db)) -> List[ReadRegion]:
    """The endpoint to get all regions

    Args:
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Raises:
        HTTPException: A 400 error code is raised if something goes wrong

    Returns:
        List[ReadRegion]: A list of all the regions in the database
    """
    try:
        return await retrieve_all_regions_service(_db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e


@regions_router.get(
    '/{_region_id}',
    description='Retrieves one region',
    status_code=status.HTTP_200_OK
)
async def retrieve_one_region_endpoint(
    _region_id: str,
    _db: Session = Depends(get_db)
) -> ReadRegion:
    """The endpoint function to retrieve a specific region

    Args:
        region_id (str): The id of the region
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        ReadRegion: The region retrieved
    """
    try:
        return await retrieve_one_region_service(_region_id, _db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e


@regions_router.post(
    '/',
    description='Creates a new region',
    status_code=status.HTTP_201_CREATED
)
async def create_region_endpoint(
    _region_data: CreateRegion,
    _db: Session = Depends(get_db)
) -> ReadRegion:
    """The endpoint function to create a new region

    Args:
        _region_data (ReadRegion): The schema for creating a region
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        ReadRegion: The newly created region
    """
    try:
        return await create_region_service(_region_data, _db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e


@regions_router.put('/{region_id}', description='Updates a region', status_code=status.HTTP_200_OK)
async def update_region_endpoint(
        _region_id: str,
        _update_region_data: UpdateRegion,
        _db: Session = Depends(get_db)) -> ReadRegion:
    """The endpoint function used to update region data

    Args:
        _region_id (str): The id of a region
        _update_region_data (UpdateRegion): The data used to update a region
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        ReadRegion: The newly updated region
    """
    try:
        return await update_region_service(_region_id, _update_region_data, _db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e


@regions_router.delete('/{region_id}', description='Deletes a region', status_code=status.HTTP_204_NO_CONTENT)
async def delete_region_endpoint(_region_id: str, _db: Session = Depends(get_db)) -> None:
    """The endpoint to delete a region from the database

    Args:
        _region_id (str): The id of the region
        _db (Session, optional): A databases session. Defaults to Depends(get_db).
    """
    try:
        return await delete_region_service(_region_id, _db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e
