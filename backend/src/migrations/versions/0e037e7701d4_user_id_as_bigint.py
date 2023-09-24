"""user id as bigint

Revision ID: 0e037e7701d4
Revises: 88e79cd1f074
Create Date: 2023-09-23 23:02:06.078935

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '0e037e7701d4'
down_revision: Union[str, None] = '88e79cd1f074'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('calendar_event', 'owner_user_id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    existing_nullable=False)
    op.alter_column('calendar_event', 'invited_user_id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    existing_nullable=False)
    op.create_unique_constraint(None, 'calendar_event', ['id'])
    op.alter_column('schedule', 'user_id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    existing_nullable=False)
    op.create_unique_constraint(None, 'schedule', ['id'])
    op.alter_column('user', 'id',
                    existing_type=sa.INTEGER(),
                    type_=sa.BigInteger(),
                    existing_nullable=False,
                    autoincrement=True)
    op.create_unique_constraint(None, 'user', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.alter_column('user', 'id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    existing_nullable=False,
                    autoincrement=True)
    op.drop_constraint(None, 'schedule', type_='unique')
    op.alter_column('schedule', 'user_id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    existing_nullable=False)
    op.drop_constraint(None, 'calendar_event', type_='unique')
    op.alter_column('calendar_event', 'invited_user_id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    existing_nullable=False)
    op.alter_column('calendar_event', 'owner_user_id',
                    existing_type=sa.BigInteger(),
                    type_=sa.INTEGER(),
                    existing_nullable=False)
    # ### end Alembic commands ###
