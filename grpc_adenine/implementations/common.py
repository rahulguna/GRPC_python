import random
import string

import grpc

from grpc_adenine.database import (connection as db)
from grpc_adenine.stubs import common_pb2
from grpc_adenine.stubs import common_pb2_grpc
from grpc_adenine.database.user_api_relation import UserApiRelation

class Common(common_pb2_grpc.CommonServicer):

	def GenerateAPIRequest(self, request, context):
		stringLength = 32
		api_key = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(stringLength))
		user_api_rel = db.query(UserApiRelation).get('1')
		return common_pb2.ApiResponse(api_key=api_key, status_message=user_api_rel.api_key, status=200)

