"""Initial migration.

Revision ID: aaba7f535b28
Revises: 9f5cd994293c
Create Date: 2024-07-31 15:09:05.717711

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'aaba7f535b28'
down_revision = '9f5cd994293c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('equipo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id_marca', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'marca', ['id_marca'], ['id'])
        batch_op.drop_column('nombre')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('equipo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nombre', mysql.VARCHAR(length=255), nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('id_marca')

    # ### end Alembic commands ###
