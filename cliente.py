import socket

HOST = input("IP del servidor (ej. 192.168.1.15): ").strip()
PORT = 5000  # Debe coincidir con el puerto del servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((HOST, PORT))
    print(f"[CLIENTE] Conectado a {HOST}:{PORT}. Escribe 'salir' para terminar.")

    while True:
        mensaje = input("Tú: ")
        cliente.sendall(mensaje.encode("utf-8"))

        respuesta = cliente.recv(1024)
        if not respuesta:
            print("[CLIENTE] El servidor cerró la conexión.")
            break
        print(f"[SERVIDOR] {respuesta.decode('utf-8')}")

        if mensaje.lower() == "salir":
            break
