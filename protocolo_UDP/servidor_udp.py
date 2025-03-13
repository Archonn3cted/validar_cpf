import socket
from validador_cpf import validate_cpf

def servidor_udp():
    host = '127.0.0.1'
    port = 5001

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print(f"Servidor UDP rodando em {host}:{port}")

    while True:
        cpf, addr = server_socket.recvfrom(1024)
        cpf = cpf.decode()
        print(f"CPF recebido: {cpf}")

        if validate_cpf(cpf):
            server_socket.sendto("CPF válido".encode(), addr)
        else:
            server_socket.sendto("CPF inválido".encode(), addr)

if __name__ == "__main__":
    servidor_udp()
