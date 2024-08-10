"""precio a detalle venta

Revision ID: a1829fa2c5d9
Revises: fddca5e640ef
Create Date: 2024-08-09 19:18:43.935275

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1829fa2c5d9'
down_revision = 'fddca5e640ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('detalle__venta', schema=None) as batch_op:
        batch_op.add_column(sa.Column('precio', sa.Numeric(precision=10, scale=2), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('detalle__venta', schema=None) as batch_op:
        batch_op.drop_column('precio')

    # ### end Alembic commands ###
