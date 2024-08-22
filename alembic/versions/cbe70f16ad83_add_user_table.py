"""add user table

Revision ID: cbe70f16ad83
Revises: 7ab20fcb86d3
Create Date: 2024-08-21 22:48:52.340404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbe70f16ad83'
down_revision = '7ab20fcb86d3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
