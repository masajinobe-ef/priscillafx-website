"""fix artists

Revision ID: 86f7ec9f3266
Revises: bf228ce01e37
Create Date: 2024-06-24 05:16:47.019503

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision: str = '86f7ec9f3266'
down_revision: Union[str, None] = 'bf228ce01e37'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'Artists',
        sa.Column('link', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artists', 'link')
    # ### end Alembic commands ###
