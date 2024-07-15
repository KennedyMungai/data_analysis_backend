"""The file containing all the services for the stores"""
from typing import List
from uuid import UUID

from sqlalchemy.orm import Session

from models.models import Stores
from schemas.stores_schema import CreateStore, ReadStore, UpdateStore


async def create_store_service(
    _store_data: CreateStore, _region_id: UUID, _db: Session
) -> ReadStore:
    """Create a store in the database.

    Args:
        _store_data (CreateStore): The schema for creating stores.
        _region_id (UUID): The ID of the region where the store is located.
        _db (Session): The database session.

    Returns:
        ReadStore: The newly created store.
    """
    store_data = _store_data.model_dump()
    store = Stores(region_id=_region_id, **store_data)

    _db.add(store)
    _db.commit()
    _db.refresh(store)

    return store


async def retrieve_all_stores_service(_db: Session) -> List[ReadStore]:
    """The service used to fetch all stores from the database

    Args:
        _db (Session): The database session

    Returns:
        List[ReadStore]: A list of the stores fetched
    """
    return _db.query(Stores).all()


async def retrieve_one_store_service(_store_id: UUID, _db: Session) -> ReadStore:
    """The service function to retrieve a specific store from the database

    Args:
        _store_id (UUID): The id of the store
        _db (Session): The database session

    Returns:
        ReadStore: The retrieved store data
    """
    return _db.query(Stores).filter(Stores.store_id == _store_id).first()


async def update_store_service(
    _store_id: UUID,
    _update_store_data: UpdateStore,
    _db: Session
) -> ReadStore:
    """The service function for updating stores in the database

    Args:
        _store_id (UUID): The id of the store in the database
        _update_store_data (UpdateStore): The schema for updating stores
        _db (Session): The database session

    Returns:
        ReadStore: The updated store
    """
    _db.query(Stores).filter(Stores.store_id == _store_id).update(
        _update_store_data.model_dump())

    _db.commit()
    return await retrieve_one_store_service(_store_id, _db)


async def delete_store_service(_store_id: UUID, _db: Session):
    """The service function for deleting stores in the database

    Args:
        _store_id (UUID): The id of the store in the database
        _db (Session): The database session
    """
    _db.query(Stores).filter(Stores.store_id == _store_id).delete()
    _db.commit()
