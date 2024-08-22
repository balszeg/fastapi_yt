"""create posts table

Revision ID: 7cf98d8a7c85
Revises: 
Create Date: 2024-08-21 20:29:12.441307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7cf98d8a7c85'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
