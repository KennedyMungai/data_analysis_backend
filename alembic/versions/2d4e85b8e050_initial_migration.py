"""Initial migration

Revision ID: 2d4e85b8e050
Revises: 
Create Date: 2024-07-15 11:27:12.874089

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '2d4e85b8e050'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('regions',
    sa.Column('region_id', sa.UUID(), server_default='gen_random_uuid()', nullable=False),
    sa.Column('region_name', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('region_id')
    )
    op.create_index(op.f('ix_regions_region_id'), 'regions', ['region_id'], unique=False)
    op.create_table('stores',
    sa.Column('store_id', sa.UUID(), server_default='gen_random_uuid()', nullable=False),
    sa.Column('store_name', sa.String(length=255), nullable=False),
    sa.Column('store_location', geoalchemy2.types.Geometry(geometry_type='POINT', from_text='ST_GeomFromEWKT', name='geometry', nullable=False), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('region_id', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['region_id'], ['regions.region_id'], ),
    sa.PrimaryKeyConstraint('store_id')
    )
    op.create_index('idx_stores_store_location', 'stores', ['store_location'], unique=False, postgresql_using='gist')
    op.create_index(op.f('ix_stores_store_id'), 'stores', ['store_id'], unique=False)
    op.create_table('employees',
    sa.Column('employee_id', sa.UUID(), server_default='gen_random_uuid()', nullable=False),
    sa.Column('employee_name', sa.String(length=255), nullable=False),
    sa.Column('employee_email', sa.String(length=255), nullable=False),
    sa.Column('employee_phone_number', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('region_id', sa.UUID(), nullable=True),
    sa.Column('store_id', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['region_id'], ['regions.region_id'], ),
    sa.ForeignKeyConstraint(['store_id'], ['stores.store_id'], ),
    sa.PrimaryKeyConstraint('employee_id')
    )
    op.create_index(op.f('ix_employees_employee_id'), 'employees', ['employee_id'], unique=False)
    op.create_table('store_sections',
    sa.Column('store_section_id', sa.UUID(), server_default='gen_random_uuid()', nullable=False),
    sa.Column('store_section_name', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('store_id', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['store_id'], ['stores.store_id'], ),
    sa.PrimaryKeyConstraint('store_section_id')
    )
    op.create_index(op.f('ix_store_sections_store_section_id'), 'store_sections', ['store_section_id'], unique=False)
    op.create_table('incidents',
    sa.Column('incident_id', sa.UUID(), server_default='gen_random_uuid()', nullable=False),
    sa.Column('incident_description', sa.Text(), nullable=False),
    sa.Column('product_name', sa.String(length=255), nullable=True),
    sa.Column('product_code', sa.String(length=50), nullable=True),
    sa.Column('product_quantity', sa.Integer(), nullable=True),
    sa.Column('product_price', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('region_id', sa.UUID(), nullable=True),
    sa.Column('store_id', sa.UUID(), nullable=True),
    sa.Column('store_section_id', sa.UUID(), nullable=True),
    sa.Column('employee_id', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.employee_id'], ),
    sa.ForeignKeyConstraint(['region_id'], ['regions.region_id'], ),
    sa.ForeignKeyConstraint(['store_id'], ['stores.store_id'], ),
    sa.ForeignKeyConstraint(['store_section_id'], ['store_sections.store_section_id'], ),
    sa.PrimaryKeyConstraint('incident_id')
    )
    op.create_index(op.f('ix_incidents_incident_id'), 'incidents', ['incident_id'], unique=False)
    op.drop_table('transactions')
    op.drop_table('categories')
    op.drop_table('accounts')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accounts',
    sa.Column('id', sa.UUID(), server_default=sa.text('gen_random_uuid()'), autoincrement=False, nullable=False),
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('plaid_id', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='accounts_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('categories',
    sa.Column('id', sa.UUID(), server_default=sa.text('gen_random_uuid()'), autoincrement=False, nullable=False),
    sa.Column('plaid_id', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.TEXT(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='categories_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('transactions',
    sa.Column('id', sa.UUID(), server_default=sa.text('gen_random_uuid()'), autoincrement=False, nullable=False),
    sa.Column('amount', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('payee', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('notes', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('accountId', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('categoryId', sa.UUID(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['accountId'], ['accounts.id'], name='transactions_accountId_accounts_id_fk', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['categoryId'], ['categories.id'], name='transactions_categoryId_categories_id_fk', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id', name='transactions_pkey')
    )
    op.drop_index(op.f('ix_incidents_incident_id'), table_name='incidents')
    op.drop_table('incidents')
    op.drop_index(op.f('ix_store_sections_store_section_id'), table_name='store_sections')
    op.drop_table('store_sections')
    op.drop_index(op.f('ix_employees_employee_id'), table_name='employees')
    op.drop_table('employees')
    op.drop_index(op.f('ix_stores_store_id'), table_name='stores')
    op.drop_index('idx_stores_store_location', table_name='stores', postgresql_using='gist')
    op.drop_table('stores')
    op.drop_index(op.f('ix_regions_region_id'), table_name='regions')
    op.drop_table('regions')
    # ### end Alembic commands ###
