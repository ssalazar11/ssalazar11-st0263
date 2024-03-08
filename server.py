import grpc
from concurrent import futures
import os
import configparser
import p2pfileshare_pb2
import p2pfileshare_pb2_grpc

# Supongamos que la configuración también incluye una lista de otros nodos de la red
def read_config(config_path='server.config'):
    config = configparser.ConfigParser()
    config.read(config_path)
    return config['PEER_CONFIG']['DIRECTORY'], config['PEER_CONFIG']['IP'], config['PEER_CONFIG']['PORT'], config.get('PEER_CONFIG', 'FRIENDS', fallback='').split(',')

class FileShareService(p2pfileshare_pb2_grpc.FileShareServiceServicer):

    def __init__(self, shared_directory, friend_nodes):
        self.shared_directory = shared_directory
        self.friend_nodes = friend_nodes

    def ListFiles(self, request, context):
        local_files = os.listdir(self.shared_directory)
        all_files = set(local_files)

        # Consulta a cada nodo amigo
        for friend in self.friend_nodes:
            if friend:  # Asegurar que el nodo amigo no esté vacío
                try:
                    channel = grpc.insecure_channel(friend)
                    friend_client = p2pfileshare_pb2_grpc.FileShareServiceStub(channel)
                    response = friend_client.ListFiles(p2pfileshare_pb2.ListFilesRequest(), timeout=5)
                    all_files.update(response.filenames)
                except Exception as e:
                    print(f"Error al consultar al amigo {friend}: {e}")

        return p2pfileshare_pb2.ListFilesResponse(filenames=list(all_files))

def serve():
    shared_directory, ip, port, friend_nodes = read_config()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    p2pfileshare_pb2_grpc.add_FileShareServiceServicer_to_server(FileShareService(shared_directory, friend_nodes), server)
    server.add_insecure_port(f'{ip}:{port}')
    server.start()
    print("Server is running...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
