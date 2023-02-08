"""auto generate rest of the tables

Revision ID: 0baf0e43d2b2
Revises: 4ee54d34ad60
Create Date: 2023-02-07 12:41:25.098399

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '0baf0e43d2b2'
down_revision = '4ee54d34ad60'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'votes',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('post_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()'),
                  nullable=False),
        sa.ForeignKeyConstraint(('post_id',), ['posts.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(('user_id',), ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('user_id', 'post_id')
    )


def downgrade() -> None:
    op.drop_table('votes')
