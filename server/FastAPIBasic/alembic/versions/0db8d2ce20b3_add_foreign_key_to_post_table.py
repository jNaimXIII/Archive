"""add foreign key to post table

Revision ID: 0db8d2ce20b3
Revises: 9950f035d8ff
Create Date: 2023-02-07 12:31:06.196617

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '0db8d2ce20b3'
down_revision = '9950f035d8ff'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('author_id', sa.Integer(), nullable=False))
    op.create_foreign_key(
        'posts_users_fk',
        source_table='posts',
        referent_table='users',
        local_cols=['author_id'],
        remote_cols=['id'], ondelete='CASCADE'
    )


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'author_id')
