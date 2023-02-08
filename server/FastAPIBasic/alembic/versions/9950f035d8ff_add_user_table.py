"""add user table

Revision ID: 9950f035d8ff
Revises: 9d5631c9fed3
Create Date: 2023-02-07 12:26:20.973282

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '9950f035d8ff'
down_revision = '9d5631c9fed3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )


def downgrade() -> None:
    op.drop_table('users')
