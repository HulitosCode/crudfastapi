"""Add created_at and updated_at columns to Todo

Revision ID: 2de42a8706f6
Revises: e1cc22c799c6
Create Date: 2024-07-03 15:36:33.651441

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2de42a8706f6'
down_revision: Union[str, None] = 'e1cc22c799c6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
