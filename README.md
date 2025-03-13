# Validação de CPF com Cliente-Servidor em TCP e UDP 👨‍💻👩‍💻

Trabalho de Sistemas Distribuídos implementando um sistema cliente-servidor para validação de CPF utilizando os protocolos TCP e UDP. A validação do CPF é feita de acordo com as regras oficiais de cálculo dos dígitos verificadores. O sistema é composto por:

- Um servidor que recebe um CPF e valida se ele é válido ou não.

- Um cliente que envia um CPF para o servidor e recebe a resposta.**Força Bruta, Algoritmo de Prim, Algoritmo de Christofides e Algoritmo de Dijkstra**.

## Autores ✍

- [Caio Henrique] (caio14.poke@gmail.com)
- [Leonardo Lima] (leo_2002_mario@hotmail.com)
- [Marcelly Silva] (marcelly.silva@arapiraca.ufal.br)

## Estrutura do Projeto

```bash
/
├── validador_cpf.py               # Função de validação do CPF (compartilhada)
├── Protocolo_TCP/                 # Pasta para implementação TCP
│   ├── servidor_tcp.py            # Servidor TCP
│   └── cliente_tcp.py             # Cliente TCP
└── Protocolo_UDP/                 # Pasta para implementação UDP
    ├── servidor_udp.py            # Servidor UDP
    └── cliente_udp.py             # Cliente UDP
```

## Funcionalidades

1. **Validação do CPF**
A função validate_cpf no arquivo validacao_cpf.py valida um CPF com base nas seguintes regras:

- O CPF deve ter exatamente 11 dígitos.

- Todos os dígitos não podem ser iguais.

- Os dígitos verificadores devem ser calculados corretamente.

2. **Servidor TCP**
O servidor TCP (servidor_tcp.py) escuta conexões na porta 5000. Quando um cliente se conecta e envia um CPF, o servidor valida o CPF e retorna uma mensagem indicando se ele é válido ou não.

3. **Servidor UDP**
O servidor UDP (servidor_udp.py) escuta pacotes na porta 5001. Quando recebe um CPF, ele valida o CPF e envia uma resposta ao cliente.

4. **Cliente TCP**
O cliente TCP (cliente_tcp.py) conecta-se ao servidor TCP, envia um CPF e exibe a resposta do servidor.

5. **Cliente UDP**
O cliente UDP (cliente_udp.py) envia um CPF para o servidor UDP e exibe a resposta recebida.

## Detalhes da Implementação

### Uso de Sockets
#### TCP (Transmission Control Protocol)
#### Servidor TCP:

- Cria um socket usando socket.socket(socket.AF_INET, socket.SOCK_STREAM).

- Associa o socket a um endereço e porta com bind().

- Escuta por conexões com listen().

- Aceita uma conexão com accept(), que retorna um novo socket para comunicação com o cliente.

- Recebe dados do cliente com recv() e envia a resposta com send().

#### Cliente TCP:

- Cria um socket usando socket.socket(socket.AF_INET, socket.SOCK_STREAM).

- Conecta-se ao servidor com connect().

- Envia o CPF com send() e recebe a resposta com recv().

#### UDP (User Datagram Protocol)
#### Servidor UDP:

- Cria um socket usando socket.socket(socket.AF_INET, socket.SOCK_DGRAM).

- Associa o socket a um endereço e porta com bind().

- Recebe pacotes de dados com recvfrom(), que retorna os dados e o endereço do cliente.

- Envia a resposta ao cliente com sendto().

#### Cliente UDP:

- Cria um socket usando socket.socket(socket.AF_INET, socket.SOCK_DGRAM).

- Envia o CPF para o servidor com sendto().

- Recebe a resposta do servidor com recvfrom().

### Validação do CPF
A função validate_cpf no arquivo validador_cpf.py realiza a validação do CPF seguindo os seguintes passos:

1. Verificação de Tamanho:

- Verifica se o CPF tem exatamente 11 dígitos.

2. Verificação de Dígitos Iguais:

- Verifica se todos os dígitos do CPF são iguais, o que invalida o CPF.

3. Cálculo dos Dígitos Verificadores:

- Calcula o primeiro dígito verificador usando os primeiros 9 dígitos do CPF.

- Calcula o segundo dígito verificador usando os primeiros 10 dígitos do CPF.

- Compara os dígitos verificadores calculados com os dígitos informados no CPF.

    
## Como Executar

### Pré-requisitos
- Python 3.x instalado.

### Passos
1. Clone o repositório:
```bash
  git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```
2. Execute o servidor TCP ou UDP:

- Para o servidor TCP:
```bash
  python servidor_tcp.py
```
- Para o servidor UDP:
```bash
  python servidor_udp.py
```
3. Execute o cliente correspondente:

- Para o cliente TCP:
```bash
  python cliente_tcp.py
```
- Para o cliente UDP:
```bash
  python cliente_udp.py
```
4. Insira o CPF para validação quando solicitado no terminal.

## Exemplo de Uso

### Servidor TCP
1. Inicie o servidor TCP:
```bash
  python servidor_tcp.py
```

2. Inicie o cliente TCP e insira um CPF:
```bash
  python cliente_tcp.py
Digite o CPF para validação: 123.456.789-09
Resposta do servidor: CPF válido
```
