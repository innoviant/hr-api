"""Initial migration

Revision ID: cdbb33e8bc07
Revises: 8bb926d1824f
Create Date: 2024-11-16 22:31:10.491073

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cdbb33e8bc07'
down_revision: Union[str, None] = '8bb926d1824f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
