import json
import argparse
import threading
from p2pclient import P2PClient
from p2pserver import app, configurar_servidor
from grpc_client import GRPCClient
from grpc_server import start_grpc_server

def cargar_configuracion(ruta_config):
    with open(ruta_config, 'r') as archivo:
        return json.load(archivo)

def iniciar_cliente_grpc(obtener_peers_actualizados, local_shared_directory, own_grpc_port):
    cliente_grpc = GRPCClient(obtener_peers_actualizados, local_shared_directory, own_grpc_port)
    
    # Interfaz de usuario para buscar archivos
    while True:
        filename = input("Ingrese el nombre del archivo a buscar (o 'exit' para salir): ")
        if filename.lower() == 'exit':
            break
        encontrado = cliente_grpc.search_file_in_peers(filename)
        if not encontrado:
            print(f"El archivo '{filename}' no se encontró en ninguno de los peers.")

def iniciar_servidor(config, cliente_p2p):
    configurar_servidor(config, cliente_p2p)
    hilo_http = threading.Thread(target=lambda: app.run(host=config['node']['ip'], port=config['node']['port']))
    hilo_http.start()
    
    # Pasa también la lista de peers conocidos al hilo gRPC
    hilo_grpc = threading.Thread(target=start_grpc_server, args=(config['resources']['shared_directory'], config['node']['grpc_port']))
    hilo_grpc.start()

    hilo_http.join()
    hilo_grpc.join()

def iniciar_cliente(cliente_p2p, mi_grpc_port, local_shared_directory):
    # Se realiza el bootstrap para descubrir peers en la red
    peers_descubiertos = cliente_p2p.realizar_bootstrap()

    # Crear una función para obtener la lista actualizada de peers
    def obtener_peers_actualizados():
        return cliente_p2p.peers_descubiertos  # Utiliza la lista actualizada de peers

    # Iniciar la interfaz de búsqueda de archivos, pasando la función para obtener peers
    iniciar_cliente_grpc(obtener_peers_actualizados, local_shared_directory, mi_grpc_port)

    if peers_descubiertos:
        print(f"Peers descubiertos por el cliente: {peers_descubiertos}")
        nuevos_peers = cliente_p2p.actualizar_peers(peers_descubiertos)
        cliente_p2p.notificar_peers(nuevos_peers)

def iniciar_nodo(config_file):
    config = cargar_configuracion(config_file)
    
    
    mi_ip = config['node']['ip']
    mi_puerto = config['node']['port']
    mi_grpc_port = config['node']['grpc_port']
    local_shared_directory = config['resources']['shared_directory']
    
    
    cliente_p2p = P2PClient(config['node']['bootstrap_peers'], mi_ip, mi_puerto, mi_grpc_port)
    
    
    hilo_servidor = threading.Thread(target=iniciar_servidor, args=(config, cliente_p2p))
    hilo_servidor.start()

    
    iniciar_cliente(cliente_p2p, mi_grpc_port, local_shared_directory)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Iniciar un nodo P2P.')
    parser.add_argument('--config', type=str, required=True, help='Ruta al archivo de configuración JSON')

    args = parser.parse_args()

    iniciar_nodo(args.config)
