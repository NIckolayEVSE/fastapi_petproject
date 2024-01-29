"""New version of tables

Revision ID: 96ac53eb3063
Revises: 4d0aeb986b8e
Create Date: 2024-01-30 01:48:42.266211

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "96ac53eb3063"
down_revision: Union[str, None] = "4d0aeb986b8e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("bookings", "room_id", existing_type=sa.INTEGER(), nullable=False)
    op.alter_column("bookings", "user_id", existing_type=sa.INTEGER(), nullable=False)
    op.alter_column(
        "hotels",
        "services",
        existing_type=postgresql.JSON(astext_type=sa.Text()),
        nullable=False,
    )
    op.alter_column("hotels", "image_id", existing_type=sa.INTEGER(), nullable=False)
    op.alter_column("rooms", "image_id", existing_type=sa.INTEGER(), nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("rooms", "image_id", existing_type=sa.INTEGER(), nullable=True)
    op.alter_column("hotels", "image_id", existing_type=sa.INTEGER(), nullable=True)
    op.alter_column(
        "hotels",
        "services",
        existing_type=postgresql.JSON(astext_type=sa.Text()),
        nullable=True,
    )
    op.alter_column("bookings", "user_id", existing_type=sa.INTEGER(), nullable=True)
    op.alter_column("bookings", "room_id", existing_type=sa.INTEGER(), nullable=True)
    # ### end Alembic commands ###
