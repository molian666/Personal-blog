"""empty message

Revision ID: 2e9527d51acc
Revises: 2c2933fca291
Create Date: 2024-11-13 23:38:17.889430

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2e9527d51acc'
down_revision = '2c2933fca291'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('attachment_db', schema=None) as batch_op:
        batch_op.alter_column('path',
               existing_type=mysql.VARCHAR(length=64),
               type_=sa.String(length=256),
               existing_comment='附件路径',
               existing_nullable=False)

    with op.batch_alter_table('comment_db', schema=None) as batch_op:
        batch_op.add_column(sa.Column('replied_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'comment_db', ['replied_id'], ['id'])

    with op.batch_alter_table('user_db', schema=None) as batch_op:
        batch_op.drop_index('name')
        batch_op.create_unique_constraint(None, ['account'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_db', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_index('name', ['name'], unique=True)

    with op.batch_alter_table('comment_db', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('replied_id')

    with op.batch_alter_table('attachment_db', schema=None) as batch_op:
        batch_op.alter_column('path',
               existing_type=sa.String(length=256),
               type_=mysql.VARCHAR(length=64),
               existing_comment='附件路径',
               existing_nullable=False)

    # ### end Alembic commands ###