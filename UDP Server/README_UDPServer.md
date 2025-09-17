
# Servidor UDP en Python

## 💻 Sobre el proyecto
Este proyecto implementa un **servidor UDP** que recibe datos enviados desde clientes o simuladores y los muestra en consola.  
Está diseñado para recibir mensajes en **formato JSON** y mostrar tanto datos estructurados como mensajes crudos en caso de error.

## 🔹 Funcionalidades
- Escucha mensajes UDP en una IP y puerto configurables.
- Recibe datos de clientes y simuladores.
- Procesa mensajes JSON y los imprime en consola.
- Muestra mensajes crudos si no tienen formato JSON válido.

## 🛠 Tecnologías utilizadas
- Python 3.x
- Socket (UDP)
- JSON
- datetime (para marcar fecha y hora de recepción)

## 📦 Archivos del proyecto
- `server.py` → Servidor UDP que recibe y procesa mensajes.
- `simulator.py` → Simula un cliente que envía datos UDP al servidor.
- `README_UDPServer.md` → Documentación del proyecto.

## 🚀 Uso
1. Ejecutar el **servidor UDP**:
```bash
python server.py
```
2. Ejecutar el **simulador** para enviar datos de prueba:
```bash
python simulator.py
```
3. Observar los datos recibidos impresos en consola.

## 👨‍💻 Autores
- Mantel Producciones - Microprocesadores  
- Ignacio Silva, Renzo Beretta y Lucas Chiappini
