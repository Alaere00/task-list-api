"""empty message

Revision ID: f9d0ca371403
Revises: 0c0ebdaf2bef
Create Date: 2022-11-06 13:58:06.841674

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9d0ca371403'
down_revision = '0c0ebdaf2bef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('goal_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'task', 'goal', ['goal_id'], ['goal_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.drop_column('task', 'goal_id')
    # ### end Alembic commands ###
