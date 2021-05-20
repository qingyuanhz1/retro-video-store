"""edited total_inventory and avaiable_inventory to video model

Revision ID: 88621cc911cb
Revises: fb4ec7b521ec
Create Date: 2021-05-18 20:40:31.006443

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '88621cc911cb'
down_revision = 'fb4ec7b521ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video', sa.Column('available_inventory', sa.Integer(), nullable=True))
    op.add_column('video', sa.Column('release_date', sa.DateTime(), nullable=True))
    op.add_column('video', sa.Column('total_inventory', sa.Integer(), nullable=True))
    op.drop_column('video', 'inventory')
    op.drop_column('video', 'released_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video', sa.Column('released_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('video', sa.Column('inventory', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('video', 'total_inventory')
    op.drop_column('video', 'release_date')
    op.drop_column('video', 'available_inventory')
    # ### end Alembic commands ###