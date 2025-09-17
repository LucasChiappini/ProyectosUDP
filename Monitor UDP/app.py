import socket
import threading
import tkinter as tk
from tkinter import ttk
import json
from datetime import datetime
import queue

UDP_IP = "0.0.0.0"
UDP_PORT = 5005
MAX_ROWS = 500

# Cola de mensajes (thread-safe)
q = queue.Queue()

def udp_listener():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    print(f"Escuchando UDP en {UDP_IP}:{UDP_PORT}")
    while True:
        try:
            data, addr = sock.recvfrom(4096)
            mensaje = data.decode("utf-8", errors="replace")
            try:
                json_data = json.loads(mensaje)
                row = (
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    json_data.get("device", ""),
                    json_data.get("counter", ""),
                    json_data.get("temp", ""),
                    json_data.get("adc0", "")
                )
            except json.JSONDecodeError:
                row = (
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "RAW",
                    addr,
                    mensaje,
                    ""
                )
            q.put(row)
        except Exception as e:
            print("Error en listener:", e)

def process_queue():
    try:
        while True:
            item = q.get_nowait()
            tree.insert("", "end", values=item)
            # Limitar filas
            children = tree.get_children()
            if len(children) > MAX_ROWS:
                tree.delete(children[0])
    except queue.Empty:
        pass
    root.after(100, process_queue)

# --- Interfaz ---
root = tk.Tk()
root.title("Monitor UDP - TSIM7000G Simulación")

columns = ("timestamp", "device", "counter", "temp", "adc0")
tree = ttk.Treeview(root, columns=columns, show="headings")

tree.heading("timestamp", text="Fecha/Hora")
tree.heading("device", text="Device")
tree.heading("counter", text="Counter")
tree.heading("temp", text="Temp (°C)")
tree.heading("adc0", text="ADC0")

tree.column("timestamp", width=150)
tree.column("device", width=120)
tree.column("counter", width=80)
tree.column("temp", width=100)
tree.column("adc0", width=80)

tree.pack(fill="both", expand=True, padx=10, pady=10)

# Iniciar hilo UDP
threading.Thread(target=udp_listener, daemon=True).start()
root.after(100, process_queue)

root.mainloop()
