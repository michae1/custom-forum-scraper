"""create topics table

Revision ID: 5545f1d1c4b
Revises: 
Create Date: 2014-12-26 16:00:28.772771

"""

# revision identifiers, used by Alembic.
revision = '5545f1d1c4b'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'topics',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.Unicode(50), nullable=False),
        sa.Column('text', sa.UnicodeText()),
   )


def downgrade():
    op.drop_table('topics')
