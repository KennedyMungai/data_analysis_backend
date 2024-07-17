"""The file containing the store sections services"""
from typing import List
from uuid import UUID

from sqlalchemy.orm import Session

from models.models import StoreSections
from schemas.store_sections_schema import (CreateStoreSection,
                                           ReadStoreSection,
                                           UpdateStoreSection)


async def create_store_section_service(
        _store_section: CreateStoreSection, _db: Session) -> ReadStoreSection:
    """The service function for creating store sections in the database

    Args:
        _store_section (CreateStoreSection): The store section data
        _db (Session): The database session
    """
    _store_section_obj = StoreSections(
        store_section_name=_store_section.store_section_name
    )
    await _db.add(_store_section_obj)
    _db.commit()
    await _db.refresh(_store_section_obj)
    return _store_section_obj


async def retrieve_single_store_section_service(
        _store_section_id: UUID, _db: Session) -> ReadStoreSection:
    """The service function for reading store sections in the database

    Args:
        _store_section_id (UUID): The store section id
        _db (Session): The database session

    Returns:
        ReadStoreSection: The store section data
    """
    return await _db.query(StoreSections).filter(
        StoreSections.store_section_id == _store_section_id
    ).first()


async def retrieve_all_store_sections_from_a_store_service(
    _store_id: UUID,
    _db: Session
) -> List[ReadStoreSection]:
    """The service function for reading all store sections in the database

    Args:
        _store_id (UUID): The store id
        _db (Session): The database session

    Returns:
        List[ReadStoreSection]: The list of store section data
    """
    return await _db.query(StoreSections).filter(StoreSections.store_id == _store_id)


async def update_store_section_service(
        _store_section_id: UUID, _store_section: UpdateStoreSection, _db: Session
) -> ReadStoreSection:
    """The service function for updating store sections in the database

    Args:
        _store_section_id (UUID): The store section id
        _store_section (UpdateStoreSection): The store section data
        _db (Session): The database session

    Returns:
        ReadStoreSection: The store section data
    """
    store = await retrieve_single_store_section_service(_store_section_id, _db)

    if not store:
        return None

    store.store_section_name = _store_section.store_section_name
    _db.commit()
    await _db.refresh(store)
    return store


async def delete_store_section_service(
        _store_section_id: UUID, _db: Session) -> None:
    """The service function for deleting store sections in the database

    Args:
        _store_section_id (UUID): The store section id
        _db (Session): The database session
    """
    await _db.query(StoreSections).filter(
        StoreSections.store_section_id == _store_section_id).delete()
    _db.commit()
