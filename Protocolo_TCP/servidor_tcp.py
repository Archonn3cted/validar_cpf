import socket
from validador_cpf import validate_cpf

def servidor_tcp():
    host = '127.0.0.1'
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Servidor TCP rodando em {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        print(f"Conexão estabelecida com {addr}")

        cpf = conn.recv(1024).decode()
        print(f"CPF recebido: {cpf}")

        if validate_cpf(cpf):
            conn.send("CPF válido".encode())
        else:
            conn.send("CPF inválido".encode())

        conn.close()

if __name__ == "__main__":
    servidor_tcp()
