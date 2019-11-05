import os
from sqlalchemy_wrapper import SQLAlchemy

# pylint: disable=invalid-name
# Connect to the database
connection = SQLAlchemy('postgresql://postgres:postgres@localhost:5432/elastos_console')