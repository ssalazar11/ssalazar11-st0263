import grpc
import os
from concurrent import futures
import grpc_service_pb2
import grpc_service_pb2_grpc

class FileSearchService(grpc_service_pb2_grpc.FileSearchServicer):
    def __init__(self, shared_directory):
        self.shared_directory = shared_directory

    def SearchFile(self, request, context):
        filename = request.filename
        print(f"Solicitud de búsqueda recibida para el archivo: {filename}")

        try:
            if self._search_local_file(filename):
                print(f"Archivo '{filename}' encontrado localmente en este nodo.")
                return grpc_service_pb2.SearchFileResponse(found=True, location="Este nodo")
            else:
                print(f"Archivo '{filename}' no encontrado localmente en este nodo.")
                return grpc_service_pb2.SearchFileResponse(found=False)
        except Exception as e:
            print(f"Error al buscar el archivo '{filename}': {e}")
            return grpc_service_pb2.SearchFileResponse(found=False)

    def _search_local_file(self, filename):
        filepath = os.path.join(self.shared_directory, filename)
        return os.path.exists(filepath)

def start_grpc_server(shared_directory, grpc_port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    file_search_service = FileSearchService(shared_directory)
    grpc_service_pb2_grpc.add_FileSearchServicer_to_server(file_search_service, server)
    server.add_insecure_port(f'[::]:{grpc_port}')
    server.start()
    print(f"gRPC server started on port {grpc_port}")
    server.wait_for_termination()
