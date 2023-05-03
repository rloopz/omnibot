#!/usr/bin/env python3
import socket
import time
import serial


esp_ip = "192.168.1.104"  # Dirección IP del ESP8266
esp_port = 80  # Puerto del servidor web del ESP8266
t = 1
# Crea un socket y establece la conexión con el ESP8266
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((esp_ip, esp_port))

# Envía los datos al ESP8266 y cierra la conexión
datos = "La maldita conexion funciona"
while t==1:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((esp_ip, esp_port))
	sock.sendall(datos.encode())
	
	time.sleep(2)
	
	sock.close()


