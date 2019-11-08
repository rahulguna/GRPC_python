import random
import string

import grpc

from smartweb_service.services.database import (
        connection as db)
from smartweb_service.services.stubs import common_pb2
from smartweb_service.services.stubs import common_pb2_grpc
from smartweb_service.services.database.user_api_relation import UserApiRelation

class Common(common_pb2_grpc.CommonServicer):

	def GenerateAPIRequest(self, request, context):
		stringLength = 32
		api_key = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(stringLength))
		user_api_rel = db.query(UserApiRelation).get('1')
		return common_pb2.ApiResponse(api_key=api_key, status_message=user_api_rel.api_key, status=200)

