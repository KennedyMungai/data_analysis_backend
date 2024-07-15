"""The routing file for the regions data"""
from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from schemas.regions_schema import ReadRegion
from sqlalchemy.orm import Session
from database.db import get_db
from services.regions_service import create_region_service, delete_region_service, retrieve_all_regions_service, retrieve_one_region_service, update_region_service


regions_router = APIRouter(prefix='/regions', tags=['Regions'])


@regions_router.get('/', description='Retrieves all regions', status_code=status.HTTP_200_OK)
async def get_all_regions(_db: Session = Depends(get_db)) -> List[ReadRegion]:
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
