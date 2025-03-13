import socket

def cliente_tcp(cpf):
    host = '127.0.0.1'
    port = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    client_socket.send(cpf.encode())

    resposta = client_socket.recv(1024).decode()
    print(f"Resposta do servidor: {resposta}")

    client_socket.close()

if __name__ == "__main__":
    cpf = input("Digite o CPF para validação: ")
    cliente_tcp(cpf)
