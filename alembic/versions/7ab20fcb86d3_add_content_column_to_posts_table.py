"""add content column to posts table

Revision ID: 7ab20fcb86d3
Revises: 7cf98d8a7c85
Create Date: 2024-08-21 20:36:15.086610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ab20fcb86d3'
down_revision = '7cf98d8a7c85'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
