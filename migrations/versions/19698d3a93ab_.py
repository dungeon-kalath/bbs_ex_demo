"""empty message

Revision ID: 19698d3a93ab
Revises: 
Create Date: 2020-01-08 00:43:42.254953

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19698d3a93ab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bbs_category',
    sa.Column('cid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('classname', sa.VARCHAR(length=60), nullable=False),
    sa.Column('parentid', sa.Integer(), nullable=False),
    sa.Column('classpath', sa.CHAR(length=20), nullable=True),
    sa.Column('relycount', sa.Integer(), nullable=False),
    sa.Column('motifcount', sa.Integer(), nullable=False),
    sa.Column('compere', sa.CHAR(length=10), nullable=True),
    sa.Column('classpic', sa.VARCHAR(length=255), nullable=False),
    sa.Column('description', sa.TEXT(length=0), nullable=True),
    sa.Column('orderby', sa.SmallInteger(), nullable=False),
    sa.Column('lastpost', sa.VARCHAR(length=255), nullable=True),
    sa.Column('namestyle', sa.CHAR(length=10), nullable=True),
    sa.Column('ispass', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('cid')
    )
    op.create_table('bbs_closeip',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ip', sa.Integer(), nullable=False),
    sa.Column('addtime', sa.Integer(), nullable=False),
    sa.Column('overtime', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bbs_comments',
    sa.Column('cmtid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ctid', sa.Integer(), nullable=False),
    sa.Column('cmtuid', sa.INTEGER(), nullable=False),
    sa.Column('cmtcontent', sa.TEXT(length=0), nullable=False),
    sa.Column('cmttime', sa.INTEGER(), nullable=False),
    sa.Column('cmtip', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('cmtid')
    )
    op.create_table('bbs_details',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tid', sa.Integer(), nullable=False),
    sa.Column('authorid', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=600), nullable=False),
    sa.Column('content', sa.TEXT(length=0), nullable=False),
    sa.Column('addtime', sa.INTEGER(), nullable=False),
    sa.Column('addip', sa.INTEGER(), nullable=False),
    sa.Column('classid', sa.INTEGER(), nullable=False),
    sa.Column('replycount', sa.INTEGER(), nullable=False),
    sa.Column('hits', sa.INTEGER(), nullable=False),
    sa.Column('istop', sa.SmallInteger(), nullable=False),
    sa.Column('elite', sa.SmallInteger(), nullable=False),
    sa.Column('ishot', sa.SmallInteger(), nullable=False),
    sa.Column('rate', sa.SmallInteger(), nullable=False),
    sa.Column('attachment', sa.SmallInteger(), nullable=True),
    sa.Column('isdel', sa.Integer(), nullable=False),
    sa.Column('style', sa.CHAR(length=10), nullable=True),
    sa.Column('isdisplay', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bbs_order',
    sa.Column('oid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('tid', sa.Integer(), nullable=False),
    sa.Column('rate', sa.Integer(), nullable=False),
    sa.Column('addtime', sa.Integer(), nullable=False),
    sa.Column('ispay', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('oid')
    )
    op.create_table('bbs_user',
    sa.Column('uid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.CHAR(length=16), nullable=False),
    sa.Column('password', sa.CHAR(length=32), nullable=False),
    sa.Column('email', sa.CHAR(length=30), nullable=False),
    sa.Column('udertype', sa.SmallInteger(), nullable=False),
    sa.Column('regtime', sa.Integer(), nullable=False),
    sa.Column('lasttime', sa.Integer(), nullable=False),
    sa.Column('regip', sa.Integer(), nullable=False),
    sa.Column('picture', sa.VARCHAR(length=255), nullable=False),
    sa.Column('grade', sa.Integer(), nullable=True),
    sa.Column('problem', sa.VARCHAR(length=200), nullable=True),
    sa.Column('result', sa.VARCHAR(length=200), nullable=True),
    sa.Column('realname', sa.CHAR(length=50), nullable=True),
    sa.Column('sex', sa.SmallInteger(), nullable=True),
    sa.Column('birthday', sa.VARCHAR(length=20), nullable=True),
    sa.Column('place', sa.VARCHAR(length=50), nullable=True),
    sa.Column('qq', sa.CHAR(length=13), nullable=True),
    sa.Column('autograph', sa.VARCHAR(length=500), nullable=True),
    sa.Column('allowlogin', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('uid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bbs_user')
    op.drop_table('bbs_order')
    op.drop_table('bbs_details')
    op.drop_table('bbs_comments')
    op.drop_table('bbs_closeip')
    op.drop_table('bbs_category')
    # ### end Alembic commands ###
