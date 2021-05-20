"""changed minor things in customer model

Revision ID: bd7072740adf
Revises: bee17dca095b
Create Date: 2021-05-18 15:29:36.975184

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'bd7072740adf'
down_revision = 'bee17dca095b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('registered_at', sa.DateTime(), nullable=True))
    op.drop_column('customer', 'register_at')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('register_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('customer', 'registered_at')
    # ### end Alembic commands ###