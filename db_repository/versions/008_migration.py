from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
grocery = Table('grocery', post_meta,
    Column('grocery_list_id', Integer, primary_key=True, nullable=False),
    Column('ingredient_id', Integer, primary_key=True, nullable=False),
    Column('units', Float),
    Column('crossed_off', Boolean),
)

grocery_list = Table('grocery_list', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
)

recipe = Table('recipe', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('description', String(length=1000)),
    Column('category', String(length=20)),
    Column('prep_time', Integer),
    Column('date_added', DateTime),
    Column('servings', Integer),
    Column('calories', Integer),
)

recipe_ingredient = Table('recipe_ingredient', post_meta,
    Column('recipe_id', Integer, primary_key=True, nullable=False),
    Column('ingredient_id', Integer, primary_key=True, nullable=False),
    Column('units', Float),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['grocery'].create()
    post_meta.tables['grocery_list'].create()
    post_meta.tables['recipe'].create()
    post_meta.tables['recipe_ingredient'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['grocery'].drop()
    post_meta.tables['grocery_list'].drop()
    post_meta.tables['recipe'].drop()
    post_meta.tables['recipe_ingredient'].drop()
