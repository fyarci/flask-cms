"""added age col to users

Revision ID: 3b4303875c75
Revises: 4d22e65ca145
Create Date: 2014-07-11 19:20:02.186610

"""

# revision identifiers, used by Alembic.
revision = '3b4303875c75'
down_revision = '4d22e65ca145'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('age', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'age')
    ### end Alembic commands ###
