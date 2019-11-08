import random
import string

import grpc

from smartweb_service.services.database import (
        connection as db)
from smartweb_service.services.stubs import did_pb2
from smartweb_service.services.stubs import did_pb2_grpc
from smartweb_service.services.database.user_api_relation import UserApiRelation

class Did(did_pb2_grpc.DidServicer):

	def Sign(self, request, context):
		stringLength = 32
		api_key = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(stringLength))
		user_api_rel = db.query(UserApiRelation).get('1')
		str1 = 'Generated Key: ' + api_key +' \nFrom Database: '+ user_api_rel.api_key
		return did_pb2.ApiResponse(message='Hey! %s' % str1, pub_key='ewfew', sig='efwe', status=200)
