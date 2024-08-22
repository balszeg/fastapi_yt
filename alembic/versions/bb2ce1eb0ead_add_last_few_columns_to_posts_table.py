"""add last few columns to posts table

Revision ID: bb2ce1eb0ead
Revises: 7cde0d9bc239
Create Date: 2024-08-22 11:35:34.191067

"""
from datetime import timezone

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb2ce1eb0ead'
down_revision = '7cde0d9bc239'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
