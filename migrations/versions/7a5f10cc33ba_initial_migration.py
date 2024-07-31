"""Initial migration.

Revision ID: 7a5f10cc33ba
Revises: 581687d54818
Create Date: 2024-07-31 15:59:28.694132

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7a5f10cc33ba'
down_revision = '581687d54818'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('equipo', schema=None) as batch_op:
        batch_op.alter_column('descripcion',
               existing_type=mysql.TEXT(),
               type_=sa.String(length=255),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('equipo', schema=None) as batch_op:
        batch_op.alter_column('descripcion',
               existing_type=sa.String(length=255),
               type_=mysql.TEXT(),
               existing_nullable=False)

    # ### end Alembic commands ###
