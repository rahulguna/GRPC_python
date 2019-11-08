from smartweb_service import settings
from sqlalchemy_wrapper import SQLAlchemy

# Connect to the database
connection = SQLAlchemy(settings.SQLALCHEMY_DATABASE_URI)