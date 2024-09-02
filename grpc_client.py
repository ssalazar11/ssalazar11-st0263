import grpc
import grpc_service_pb2
import grpc_service_pb2_grpc
import os
import time

class GRPCClient:
    def __init__(self, obtener_peers_actualizados, local_shared_directory, own_grpc_port, intervalo_reintentos=5):
        self.obtener_peers_actualizados = obtener_peers_actualizados  # Función para obtener la lista actualizada de peers
        self.local_shared_directory = local_shared_directory  # Directorio compartido local
        self.own_grpc_port = own_grpc_port  # Puerto gRPC del nodo actual
        self.intervalo_reintentos = intervalo_reintentos  # Intervalo entre reintentos

    def search_file_in_local_directory(self, filename):
        file_path = os.path.join(self.local_shared_directory, filename)
        if os.path.exists(file_path):
            print(f"Archivo '{filename}' encontrado localmente en {self.local_shared_directory}")
            return True
        return False

    def search_file_in_peers(self, filename):
        if not filename:
            print("Error: el nombre del archivo está vacío. Por favor, proporciona un nombre de archivo válido.")
            return False

        # Verificar en el directorio local primero
        if self.search_file_in_local_directory(filename):
            return True

        while True:  # Bucle infinito para intentar la búsqueda continuamente
            print(f"Buscando el archivo '{filename}' en los peers...")
            peers = self.obtener_peers_actualizados()  # Obtener la lista actualizada de peers

            for peer in peers:
                ip = peer['ip']
                grpc_port = peer['grpc_port']

                if grpc_port:
                    # Evitar buscar en el propio nodo
                    if grpc_port == self.own_grpc_port:
                        continue

                    address = f"{ip}:{grpc_port}"
                    print(f"Intentando conectar al nodo {address} para buscar '{filename}'...")

                    try:
                        with grpc.insecure_channel(address) as channel:
                            stub = grpc_service_pb2_grpc.FileSearchStub(channel)
                            request = grpc_service_pb2.SearchFileRequest(filename=filename)
                            response = stub.SearchFile(request)

                            if response.found:
                                print(f"Archivo '{filename}' encontrado en el nodo {address}, ubicación: {response.location}")
                                return True
                            else:
                                print(f"Archivo '{filename}' no encontrado en el nodo {address}.")
                    except Exception as e:
                        print(f"Error al conectar con el nodo {address} para buscar archivo: {e}")

            print(f"El archivo '{filename}' no se encontró en los peers actuales. Reintentando en {self.intervalo_reintentos} segundos...")
            time.sleep(self.intervalo_reintentos)  # Espera antes de reintentar
