import datetime
import pytz
from grpc_adenine.database import (connection as db)
from grpc_adenine.database.user_api_relation import UserApiRelation

def validate_api_key(api_key):
	user_api_rel = UserApiRelation.query.filter(UserApiRelation.api_key == api_key).first()
	#print db.query(exists().where(UserApiRelation.api_key == 'KHBOsth7b3WbOTVzZqGUEhOY8rPreYFM')).scalar()
	if user_api_rel is None:
		return False
	return True

def getTime():
	return datetime.datetime.now(pytz.timezone('America/New_York')).strftime("%Y-%m-%d %H:%M:%S %z")
