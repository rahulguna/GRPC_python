from __future__ import print_function
import logging

import grpc

from smartweb_service.services.stubs import common_pb2
import smartweb_service.services.stubs.common_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = common_pb2_grpc.CommonStub(channel)
        response = stub.GenerateAPIRequest(common_pb2.ApiRequest(name='hey'))
    print("SmartWeb client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()