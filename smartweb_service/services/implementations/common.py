import random
import string

import grpc

from smartweb_service.services.stubs import common_pb2
from smartweb_service.services.stubs import common_pb2_grpc

class Common(common_pb2_grpc.CommonServicer):

	def GenerateAPIRequest(self, request, context):
		stringLength = 32
		api_key = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(stringLength))
		return common_pb2.ApiResponse(message='Hey! \n API Key: %s' % api_key)

