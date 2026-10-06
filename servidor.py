import socket

# Configuración del servidor
# '0.0.0.0' permite escuchar peticiones de cualquier interfaz de red local
HOST = '0.0.0.0'  
PORT = 5000       # Puerto donde escuchará (puedes usar cualquier puerto libre > 1024)

# Crear el socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el socket a la dirección y puerto
server_socket.bind((HOST, PORT))

# Poner el servidor en modo escucha (máximo 1 cliente en espera)
server_socket.listen(1)
print(f"[*] Servidor escuchando en el puerto {PORT}...")

# Aceptar la conexión entrante
client_socket, client_address = server_socket.accept()
print(f"[+] Conexión establecida desde: {client_address}")

try:
    while True:
        # Recibir mensaje del cliente (hasta 1024 bytes)
        data = client_socket.recv(1024)
        if not data:
            break  # El cliente se desconectó
        
        mensaje = data.decode('utf-8')
        print(f"Cliente: {mensaje}")
        
        # Responder al cliente
        respuesta = f"Servidor recibió: {mensaje}"
        client_socket.sendall(respuesta.encode('utf-8'))

finally:
    # Cerrar las conexiones al finalizar
    client_socket.close()
    server_socket.close()
    print("[-] Conexión cerrada.")