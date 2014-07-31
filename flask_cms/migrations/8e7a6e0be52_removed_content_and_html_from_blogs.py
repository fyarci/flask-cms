"""removed content and html from blogs

Revision ID: 8e7a6e0be52
Revises: 38f92517fc81
Create Date: 2014-07-20 00:16:08.543272

"""

# revision identifiers, used by Alembic.
revision = '8e7a6e0be52'
down_revision = '38f92517fc81'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogs', 'content')
    op.drop_column('blogs', 'html')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('html', mysql.TEXT(), nullable=True))
    op.add_column('blogs', sa.Column('content', mysql.TEXT(), nullable=True))
    ### end Alembic commands ###
