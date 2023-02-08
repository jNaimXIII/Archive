"""add content column to post table

Revision ID: 9d5631c9fed3
Revises: d863db7493fc
Create Date: 2023-02-07 12:23:16.920105

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '9d5631c9fed3'
down_revision = 'd863db7493fc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
