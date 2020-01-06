"""last exception

Revision ID: b6a68a3b04cc
Revises: 77d5d9ff936f
Create Date: 2020-01-05 17:08:48.703885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6a68a3b04cc'
down_revision = '77d5d9ff936f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_exception', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_exception')
    # ### end Alembic commands ###
