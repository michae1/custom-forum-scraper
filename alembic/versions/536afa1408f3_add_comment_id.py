"""add comment id

Revision ID: 536afa1408f3
Revises: 5545f1d1c4b
Create Date: 2014-12-26 22:15:39.813053

"""

# revision identifiers, used by Alembic.
revision = '536afa1408f3'
down_revision = '5545f1d1c4b'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('topics', sa.Column('comment_id', sa.Unicode(50)))

def downgrade():
    op.drop_column('topics', 'comment_id')