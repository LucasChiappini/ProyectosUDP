#Este simulator sirve como simular el SIM7000G que vamos a usar.

# Importamos módulos necesarios:
# socket -> para enviar datos a través de la red
# time -> para pausas entre envíos
# json -> para convertir diccionarios de Python a cadenas JSON
import socket, time, json

# Dirección IP del servidor UDP al que se enviarán los datos
UDP_IP = "127.0.0.1"  # localhost, mismo equipo

# Puerto del servidor UDP
UDP_PORT = 5005

# Crea un socket UDP (SOCK_DGRAM) usando IPv4 (AF_INET)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bucle que enviará 5 mensajes de prueba
for i in range(5):
    # Crea un diccionario con datos simulados
    msg = {
        "device": "TSIM7000G",    # Nombre del dispositivo
        "counter": i,              # Contador incremental
        "temp": 20.0 + i * 0.5,    # Temperatura simulada que aumenta cada iteración
        "adc0": i * 10             # Valor de ADC simulado
    }
    
    # Convierte el diccionario a JSON, lo codifica en bytes y lo envía al servidor UDP
    sock.sendto(json.dumps(msg).encode(), (UDP_IP, UDP_PORT))
    
    # Imprime en consola el mensaje enviado
    print("Enviado:", msg)
    
    # Espera 1 segundo antes de enviar el siguiente mensaje
    time.sleep(1)
