from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Variables globales para IP, Puerto, Directorio, y Peers
IP = "0.0.0.0"
PORT = 0
GRPC_PORT = 0
SHARED_DIRECTORY = "./shared_files"
CLIENTE_P2P = None
PEERS = []

def configurar_servidor(config, cliente_p2p):
    global IP, PORT, GRPC_PORT, SHARED_DIRECTORY, CLIENTE_P2P
    IP = config['node']['ip']
    PORT = config['node']['port']
    GRPC_PORT = config['node']['grpc_port']
    SHARED_DIRECTORY = config['resources']['shared_directory']
    CLIENTE_P2P = cliente_p2p
    print(f"Configuración del servidor cargada: Directorio compartido en {SHARED_DIRECTORY}")

def actualizar_peers(nuevos_peers):
    global PEERS
    for peer in nuevos_peers:
        if peer not in PEERS:
            PEERS.append(peer)
    print(f"Lista de peers actualizada en el nodo: {PEERS}")

@app.route('/discover', methods=['GET'])
def discover():
    global PEERS, IP, PORT, GRPC_PORT
    self_peer = {"ip": IP, "http_port": PORT, "grpc_port": GRPC_PORT}
    if self_peer not in PEERS:
        PEERS.append(self_peer)
    
    print(f"Lista de peers conocida en este nodo: {PEERS}")
    return jsonify({"peers": PEERS})


@app.route('/updatePeers', methods=['POST'])
def update_peers():
    nuevos_peers = request.json.get('peers', [])
    if nuevos_peers:
        peers_no_conocidos = [peer for peer in nuevos_peers if peer not in PEERS]
        if peers_no_conocidos:
            print(f"Recibidos nuevos peers para actualización: {peers_no_conocidos}")
            actualizar_peers(peers_no_conocidos)
            print(f"Lista de peers actualizada después de notificación: {PEERS}")
            
            CLIENTE_P2P.notificar_peers(peers_no_conocidos)
        else:
            print("No hay peers nuevos que propagar.")
        
        return jsonify({"message": "Lista de peers actualizada"}), 200
    return jsonify({"error": "No se proporcionaron peers"}), 400

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    print(f"Solicitud de descarga para el archivo: {filename}")
    return jsonify({"status": "Archivo descargado exitosamente", "filename": filename}), 200


@app.route('/upload/<filename>', methods=['GET'])
def upload_file(filename):

    print(f"Archivo recibido para subir: {filename}")
    return jsonify({"status": "Archivo subido exitosamente", "filename": filename}), 200