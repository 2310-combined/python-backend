from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '6354e11530fb'
down_revision = 'b600367ac862'
branch_labels = None
depends_on = None

def upgrade():
    # Adding new columns initially as nullable to avoid constraints on existing data
    with op.batch_alter_table('trips', schema=None) as batch_op:
        batch_op.add_column(sa.Column('start_location_latitude', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('start_location_longitude', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('end_location_latitude', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('end_location_longitude', sa.String(length=50), nullable=True))

    # Assuming you can derive these values or set a default
    op.execute("""
               UPDATE trips
               SET start_location_latitude = 'default-latitude', -- Put appropriate default or derived value
                   start_location_longitude = 'default-longitude', -- Put appropriate default or derived value
                   end_location_latitude = 'default-latitude', -- Put appropriate default or derived value
                   end_location_longitude = 'default-longitude' -- Put appropriate default or derived value
               """)

    # Now alter the nullability once all data is populated
    with op.batch_alter_table('trips', schema=None) as batch_op:
        batch_op.alter_column('start_location_latitude', nullable=False)
        batch_op.alter_column('start_location_longitude', nullable=False)
        batch_op.alter_column('end_location_latitude', nullable=False)
        batch_op.alter_column('end_location_longitude', nullable=False)

    # Drop the old columns if they are now redundant
    with op.batch_alter_table('trips', schema=None) as batch_op:
        batch_op.drop_column('start_location')
        batch_op.drop_column('end_location')

def downgrade():
    # To downgrade, reintroduce the old columns with defaults and remove the new ones
    with op.batch_alter_table('trips', schema=None) as batch_op:
        batch_op.add_column(sa.Column('start_location', sa.String(length=255), nullable=False, server_default='{}'))
        batch_op.add_column(sa.Column('end_location', sa.String(length=255), nullable=False, server_default='{}'))
        
        batch_op.drop_column('start_location_latitude')
        batch_op.drop_column('start_location_longitude')
        batch_op.drop_column('end_location_latitude')
        batch_op.drop_column('end_location_longitude')
