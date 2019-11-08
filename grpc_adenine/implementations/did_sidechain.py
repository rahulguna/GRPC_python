import random
import string

import grpc

from grpc_adenine.database import (connection as db)
from grpc_adenine.stubs import did_pb2
from grpc_adenine.stubs import did_pb2_grpc
from grpc_adenine.database.user_api_relation import UserApiRelation

class Did(did_pb2_grpc.DidServicer):

	def Sign(self, request, context):
		stringLength = 32
		api_key = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(stringLength))
		user_api_rel = db.query(UserApiRelation).get('1')
		str1 = 'Generated Key: ' + api_key +' \nFrom Database: '+ user_api_rel.api_key
		return did_pb2.ApiResponse(message='Hey! %s' % str1, pub_key='ewfew', sig='efwe', status=200)
