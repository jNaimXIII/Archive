"""add phone number column to user table

Revision ID: 6f4a9f3feab5
Revises: 0baf0e43d2b2
Create Date: 2023-02-07 12:44:54.883336

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '6f4a9f3feab5'
down_revision = '0baf0e43d2b2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
