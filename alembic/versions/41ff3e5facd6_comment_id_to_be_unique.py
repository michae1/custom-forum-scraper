"""comment id to be unique

Revision ID: 41ff3e5facd6
Revises: 536afa1408f3
Create Date: 2014-12-28 17:57:44.761988

"""

# revision identifiers, used by Alembic.
revision = '41ff3e5facd6'
down_revision = '536afa1408f3'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_unique_constraint("uq_comment_id", "topics", ["comment_id"])


def downgrade():
    op.drop_unique_constraint("uq_comment_id", "topics")
