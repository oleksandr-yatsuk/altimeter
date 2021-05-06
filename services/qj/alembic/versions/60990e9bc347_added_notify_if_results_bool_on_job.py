"""added notify_if_results bool on job

Revision ID: 60990e9bc347
Revises: dc8f1df07766
Create Date: 2021-05-06 07:51:08.854424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60990e9bc347'
down_revision = 'dc8f1df07766'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job', sa.Column('notify_if_results', sa.Boolean(), server_default='false', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('job', 'notify_if_results')
    # ### end Alembic commands ###
