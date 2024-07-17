"""The file containing the services for the regions"""
from typing import List

from sqlalchemy.orm import Session

from models.models import Regions
from schemas.regions_schema import CreateRegion, ReadRegion, UpdateRegion


async def create_region_service(_region_data: CreateRegion, _db: Session) -> ReadRegion:
    """The service function for creating regions in the database

    Args:
        _region_data (CreateRegion): The schema for creating regions
        _db (Session): Database session

    Returns:
        ReadRegion: The newly created region
    """
    region = Regions(**_region_data.model_dump())
    await _db.add(region)
    _db.commit()
    await _db.refresh(region)
    return region


async def retrieve_all_regions_service(_db: Session) -> List[ReadRegion]:
    """The service used to fetch all regions from the database

    Args:
        _db (Session): The database session

    Returns:
        List[ReadRegion]: A list of the regions fetched
    """
    return await _db.query(Regions).all()


async def retrieve_one_region_service(_region_id: str, _db: Session) -> ReadRegion:
    """The service function to retrieve a specific region from the database

    Args:
        _region_id (str): The id of the region
        _db (Session): The database session

    Returns:
        ReadRegion: The retrieved region data
    """
    return await _db.query(Regions).filter(Regions.region_id == _region_id).first()


async def update_region_service(
    _region_id: str,
    _update_region_data: UpdateRegion,
    _db: Session
) -> ReadRegion:
    """The service function for updating regions in the database

    Args:
        _region_id (str): The id of the region in the database
        _region_data (UpdateRegion): The data used to update the region
        _db (Session): The database session

    Returns:
        ReadRegion: The newly update region info
    """
    region = await retrieve_one_region_service(_region_id, _db)

    if not region:
        return

    region.region_name = _update_region_data.region_name

    _db.commit()
    await _db.refresh(region)
    return region


async def delete_region_service(_region_id: str, _db: Session) -> None:
    """The service function for deleting regions in the database

    Args:
        _region_id (str): The id of the region in the database
        _db (Session): The database session
    """
    region = await retrieve_one_region_service(_region_id, _db)

    if not region:
        return

    await _db.delete(region)
    _db.commit()
