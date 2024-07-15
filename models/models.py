"""The file containing the models for the application"""
from datetime import datetime

from sqlalchemy import UUID, Boolean, Column, DateTime, String, Text, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry

from database.db import Base


class Regions(Base):
    """The model for region data

    Args:
        Base (_type_): Declarative Base instance
    """
    __tablename__ = 'regions'

    region_id = Column(UUID, primary_key=True, index=True,
                       server_default='gen_random_uuid()')
    region_name = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, nullable=True, onupdate=datetime.now())

    stores = relationship('Stores', back_populates='region')
    employees = relationship('Employees', back_populates='region')
    incidents = relationship('Incidents', back_populates='region')


class Stores(Base):
    """The model for the stores

    Args:
        Base (Base): Declarative Base instance
    """
    __tablename__ = 'stores'

    store_id = Column(UUID, primary_key=True, index=True,
                      server_default='gen_random_uuid()')
    store_name = Column(String(255), nullable=False)
    store_location = Column(Geometry('POINT'), nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, nullable=True, onupdate=datetime.now())

    region_id = Column(UUID, ForeignKey('regions.region_id'))

    employees = relationship('Employees', back_populates='store')
    incidents = relationship('Incidents', back_populates='store')
    store_sections = relationship('StoreSections', back_populates='store')


class Employees(Base):
    """The model for employee data

    Args:
        Base (_type_): Declarative Base instance
    """
    __tablename__ = 'employees'

    employee_id = Column(UUID, primary_key=True, index=True,
                         server_default='gen_random_uuid()')
    employee_name = Column(String(255), nullable=False)
    employee_email = Column(String(255), nullable=False)
    employee_phone_number = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, nullable=True, onupdate=datetime.now())
    is_active = Column(Boolean, default=True, nullable=False)

    region_id = Column(UUID, ForeignKey('regions.region_id'))
    store_id = Column(UUID, ForeignKey('stores.store_id'))

    incidents = relationship('Incidents', back_populates='employee')


class StoreSections(Base):
    """The model for store sections

    Args:
        Base (_type_): Declarative Base Instance
    """
    __tablename__ = 'store_sections'

    store_section_id = Column(UUID, primary_key=True, index=True,
                              server_default='gen_random_uuid()')
    store_section_name = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, nullable=True, onupdate=datetime.now())

    store_id = Column(UUID, ForeignKey('stores.store_id'))

    incidents = relationship('Incidents', back_populates='store_section')


class Incidents(Base):
    """The model for incidents

    Args:
        Base (_type_): Declarative Base Instance
    """
    __tablename__ = 'incidents'

    incident_id = Column(UUID, primary_key=True, index=True,
                         server_default='gen_random_uuid()')
    incident_description = Column(Text, nullable=False)
    product_name = Column(String(255), nullable=True)
    product_code = Column(String(50), nullable=True)
    product_quantity = Column(Integer, nullable=True)
    product_price = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, nullable=True, onupdate=datetime.now())

    region_id = Column(UUID, ForeignKey('regions.region_id'))
    store_id = Column(UUID, ForeignKey('stores.store_id'))
    store_section_id = Column(UUID, ForeignKey(
        'store_sections.store_section_id'))
    employee_id = Column(UUID, ForeignKey('employees.employee_id'))

    employee = relationship('Employees', back_populates='incidents')
    region = relationship('Regions', back_populates='incidents')
    store = relationship('Stores', back_populates='incidents')
    store_section = relationship('StoreSections', back_populates='incidents')
