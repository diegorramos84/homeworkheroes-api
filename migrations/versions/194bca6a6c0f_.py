"""empty message

Revision ID: 194bca6a6c0f
Revises: 5e41f110dc4c
Create Date: 2023-06-18 19:56:06.536518

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '194bca6a6c0f'
down_revision = '5e41f110dc4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('school', sa.String(length=50), nullable=False),
    sa.Column('school_class', sa.String(length=50), nullable=False),
    sa.Column('superpower', sa.String(length=50), nullable=True),
    sa.Column('date_of_birth', sa.DateTime(), nullable=False),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('password', sa.String(length=130), nullable=False),
    sa.Column('avatar', sa.String(length=200), nullable=True),
    sa.Column('date_created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('role', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('school', sa.String(length=50), nullable=False),
    sa.Column('school_class', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('date_created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('role', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('homework',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('homework_name', sa.String(length=500), nullable=True),
    sa.Column('subject', sa.String(length=500), nullable=False),
    sa.Column('content', sa.String(length=500), nullable=False),
    sa.Column('extra_resources', sa.String(length=500), nullable=True),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('assignments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('deadline', sa.DateTime(timezone=True), nullable=False),
    sa.Column('teacher_feedback', sa.String(length=500), nullable=True),
    sa.Column('student_feedback', sa.String(length=500), nullable=True),
    sa.Column('completed', sa.Boolean(), server_default=sa.text('false'), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('homework_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['homework_id'], ['homework.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('assignments')
    op.drop_table('homework')
    op.drop_table('teachers')
    op.drop_table('students')
    # ### end Alembic commands ###
