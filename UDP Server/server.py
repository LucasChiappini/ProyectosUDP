# Importa el módulo socket para crear y manejar conexiones de red
import socket

# Importa el módulo json para convertir entre cadenas JSON y objetos de Python
import json

# Importa datetime para obtener la fecha y hora actual
from datetime import datetime

# Dirección IP en la que el servidor escuchará (0.0.0.0 significa todas las interfaces)
UDP_IP = "0.0.0.0"

# Puerto en el que el servidor escuchará
UDP_PORT = 5005

# Función principal que ejecuta el servidor UDP
def run_server():
    # Crea un socket UDP (SOCK_DGRAM) usando IPv4 (AF_INET)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Vincula el socket a la IP y puerto definidos
    sock.bind((UDP_IP, UDP_PORT))
    
    # Imprime mensaje indicando que el servidor está listo para recibir datos
    print(f"Servidor UDP escuchando en {UDP_IP}:{UDP_PORT}...")

    # Bucle infinito para mantener el servidor corriendo y recibiendo mensajes
    while True:
        # Recibe datos del socket. 4096 es el tamaño máximo del buffer. Devuelve datos y dirección del cliente.
        data, addr = sock.recvfrom(4096)
        try:
            # Decodifica los datos recibidos de bytes a cadena UTF-8
            mensaje = data.decode("utf-8", errors="replace")
            
            # Intenta convertir la cadena decodificada a un objeto JSON de Python
            json_data = json.loads(mensaje)
            
            # Imprime la fecha/hora, dirección del remitente y el contenido JSON recibido
            print(f"[{datetime.now()}] {addr} -> {json_data}")
        except json.JSONDecodeError:
            # Si no se puede decodificar como JSON, imprime los datos crudos recibidos
            print(f"[{datetime.now()}] {addr} -> RAW: {mensaje}")

# Si el archivo se ejecuta directamente (no importado), se llama a la función principal
if __name__ == "__main__":
    run_server()
