"""activo boolean en proveedor

Revision ID: 3f5bb21dc570
Revises: bd5ccaa6cdcb
Create Date: 2024-08-06 22:30:01.072677

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3f5bb21dc570'
down_revision = 'bd5ccaa6cdcb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('proveedor', schema=None) as batch_op:
        batch_op.alter_column('activo',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Integer(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('proveedor', schema=None) as batch_op:
        batch_op.alter_column('activo',
               existing_type=sa.Integer(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False)

    # ### end Alembic commands ###
