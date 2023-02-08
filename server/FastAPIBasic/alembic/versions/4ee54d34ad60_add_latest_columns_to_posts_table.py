"""add latest columns to posts table

Revision ID: 4ee54d34ad60
Revises: 0db8d2ce20b3
Create Date: 2023-02-07 12:35:28.783175

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '4ee54d34ad60'
down_revision = '0db8d2ce20b3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),
    )
    op.add_column(
        'posts',
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()'))
    )


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
