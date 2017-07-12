
""" Module summary:
Variables:
  db_session - A connection to the farmfinder database.
"""

import os

from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from dbsetup import Base

from runpy import run_path

############################################################################


# Connect to database and create database session:
DATABASE_URI = os.environ['DATABASE_URI']


engine = create_engine(DATABASE_URI)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

db_session = DBSession()

#Session = scoped_session(DBSession)
#db_session = Session()

