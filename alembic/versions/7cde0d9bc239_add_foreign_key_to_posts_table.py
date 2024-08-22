"""add foreign-key to posts table

Revision ID: 7cde0d9bc239
Revises: cbe70f16ad83
Create Date: 2024-08-21 22:55:12.891994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7cde0d9bc239'
down_revision = 'cbe70f16ad83'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
