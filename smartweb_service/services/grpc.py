from concurrent import futures
import logging

import grpc

from smartweb_service.services.stubs import common_pb2
import smartweb_service.services.stubs.common_pb2_grpc

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    common_pb2_grpc.add_CommonServicer_to_server(Common(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()