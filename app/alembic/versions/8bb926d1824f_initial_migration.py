"""Initial migration

Revision ID: 8bb926d1824f
Revises: 8b1264ea407c
Create Date: 2024-11-16 22:23:54.606630

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8bb926d1824f'
down_revision: Union[str, None] = '8b1264ea407c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
