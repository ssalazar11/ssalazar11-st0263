import time
import requests

class P2PClient:
    def __init__(self, bootstrap_peers, mi_ip, mi_puerto, grpc_port, max_reintentos=2, intervalo_reintentos=10):
        self.peers_descubiertos = []
        self.bootstrap_peers = bootstrap_peers
        self.mi_ip = mi_ip
        self.mi_puerto = mi_puerto
        self.grpc_port = grpc_port
        self.max_reintentos = max_reintentos
        self.intervalo_reintentos = intervalo_reintentos

    def realizar_bootstrap(self):
        peers_totales = []

        for reintento in range(self.max_reintentos):
            for peer in self.bootstrap_peers:
                try:
                    ip, port = peer.split(":")
                    url = f"http://{ip}:{port}/discover"
                    response = requests.get(url)
                    if response.status_code == 200:
                        nuevos_peers = response.json().get('peers', [])
                        print(f"Conectado exitosamente a {peer}. Peers descubiertos: {nuevos_peers}")

                        for nuevo_peer in nuevos_peers:
                            if nuevo_peer not in peers_totales:
                                peers_totales.append(nuevo_peer)

                        nuevos_peers_descubiertos = self.actualizar_peers(nuevos_peers)
                        self.notificar_propio_peer(nuevos_peers_descubiertos)

                        if nuevos_peers_descubiertos:
                            self.notificar_peers(nuevos_peers_descubiertos)

                except Exception as e:
                    print(f"No se pudo conectar al peer semilla {peer}: {e}")
            print(f"Reintento {reintento + 1} de {self.max_reintentos} fallido. Esperando {self.intervalo_reintentos} segundos antes de reintentar.")
            time.sleep(self.intervalo_reintentos)
        
        if peers_totales:
            return peers_totales
        else:
            print("No se pudo conectar a ningún peer semilla después de múltiples reintentos.")
            return []
        
    def notificar_propio_peer(self, nuevos_peers):
        for peer in nuevos_peers:
            try:
                ip = peer['ip']
                port = peer['http_port']
                url = f"http://{ip}:{port}/updatePeers"
                response = requests.post(url, json={"peers": [{"ip": self.mi_ip, "http_port": self.mi_puerto, "grpc_port": self.grpc_port}]})
                if response.status_code == 200:
                    print(f"Dirección de este nodo notificada exitosamente a {peer}.")
                else:
                    print(f"Error al notificar la dirección de este nodo a {peer}: {response.status_code}")
            except Exception as e:
                print(f"Error al conectar con el peer {peer} para notificar la dirección de este nodo: {e}")

    def actualizar_peers(self, nuevos_peers):
        peers_nuevos_descubiertos = []
        for peer in nuevos_peers:
            if peer not in self.peers_descubiertos:
                self.peers_descubiertos.append(peer)
                peers_nuevos_descubiertos.append(peer)
        print(f"Lista de peers actualizada: {self.peers_descubiertos}")
        return peers_nuevos_descubiertos

    def notificar_peers(self, nuevos_peers):
        for peer in nuevos_peers:
            try:
                ip = peer['ip']
                port = peer['http_port']
                url = f"http://{ip}:{port}/updatePeers"
                response = requests.post(url, json={"peers": self.peers_descubiertos})
                if response.status_code == 200:
                    print(f"Peers actualizados exitosamente en {peer}.")
                else:
                    print(f"Error al actualizar peers en {peer}: {response.status_code}")
            except Exception as e:
                print(f"Error al conectar con el peer {peer} para actualizar peers: {e}")
