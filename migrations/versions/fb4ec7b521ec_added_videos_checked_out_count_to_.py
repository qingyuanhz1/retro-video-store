"""added videos_checked_out_count to customer model

Revision ID: fb4ec7b521ec
Revises: f1af87932972
Create Date: 2021-05-18 17:46:14.106444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb4ec7b521ec'
down_revision = 'f1af87932972'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('videos_checked_out_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customer', 'videos_checked_out_count')
    # ### end Alembic commands ###