"""changed post structure

Revision ID: 6eb77eae96f8
Revises: 3b2d804f8ae4
Create Date: 2018-09-28 21:54:37.960759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6eb77eae96f8'
down_revision = '3b2d804f8ae4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('diplomat_id', sa.Integer(), nullable=False))
    op.drop_constraint('post_diplomat_fkey', 'post', type_='foreignkey')
    op.create_foreign_key(None, 'post', 'diplomat', ['diplomat_id'], ['uid'])
    op.drop_column('post', 'diplomat')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('diplomat', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.create_foreign_key('post_diplomat_fkey', 'post', 'diplomat', ['diplomat'], ['uid'])
    op.drop_column('post', 'diplomat_id')
    # ### end Alembic commands ###
