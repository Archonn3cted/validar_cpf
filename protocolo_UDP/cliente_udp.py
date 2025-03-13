import socket

def cliente_udp(cpf):
    host = '127.0.0.1'
    port = 5001

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    client_socket.sendto(cpf.encode(), (host, port))

    resposta, addr = client_socket.recvfrom(1024)
    print(f"Resposta do servidor: {resposta.decode()}")

    client_socket.close()

if __name__ == "__main__":
    cpf = input("Digite o CPF para validação: ")
    cliente_udp(cpf)
