import random
import string
import os
import grpc

from grpc_adenine.database import (connection as db)
from grpc_adenine.stubs import common_pb2
from grpc_adenine.stubs import common_pb2_grpc
from grpc_adenine.database.user_api_relation import UserApiRelation
from sqlalchemy.sql import exists

class Common(common_pb2_grpc.CommonServicer):

	def GenerateAPIRequest(self, request, context):
		stringLength = 32
		secret_key = os.environ['SHARED_SECRET_ADENINE']
	
		if(secret_key==request.secret_key):
			api_key = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(stringLength))
			return common_pb2.ApiResponse(api_key=api_key, status_message='Success', status=200)
		else:
			return common_pb2.ApiResponse(api_key='', status_message='Authentication Error', status=400)


