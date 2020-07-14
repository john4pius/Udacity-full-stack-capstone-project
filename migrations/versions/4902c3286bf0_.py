"""empty message

Revision ID: 4902c3286bf0
Revises: 
Create Date: 2020-07-14 17:35:50.658499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4902c3286bf0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('persons')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('persons',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='persons_pkey')
    )
    # ### end Alembic commands ###