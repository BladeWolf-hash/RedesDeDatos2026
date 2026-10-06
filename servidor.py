import socket

HOST = "0.0.0.0"   # Escucha en todas las interfaces de red del equipo
PORT = 5000        # Puerto (usar >1024); debe ser el mismo en el cliente

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind((HOST, PORT))
    servidor.listen()
    print(f"[SERVIDOR] Esperando conexiones en el puerto {PORT}...")

    conexion, direccion = servidor.accept()
    with conexion:
        print(f"[SERVIDOR] Cliente conectado desde {direccion}")
        while True:
            datos = conexion.recv(1024)
            if not datos:  # El cliente cerró la conexión
                print("[SERVIDOR] Cliente desconectado.")
                break

            mensaje = datos.decode("utf-8")
            print(f"[CLIENTE] {mensaje}")

            if mensaje.lower() == "salir":
                conexion.sendall("Conexión finalizada.".encode("utf-8"))
                break

            # Respuesta del servidor (aquí puedes poner tu propia lógica)
            respuesta = f"Servidor recibió: {mensaje}"
            conexion.sendall(respuesta.encode("utf-8"))
