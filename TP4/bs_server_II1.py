import argparse
import socket
import sys
import logging

logging.basicConfig( format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG,filename='/var/log/bs_server/bs_server.log', encoding='utf-8')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

logging.getLogger().addHandler(console_handler)

def check_port(value):
    logging.info(f"Le serveur tourne sur 10.1.1.10:{args.port}")
    
    try:
        port = int(value)
        if port < 0 or port > 65535:
            print("ERROR: Le port spécifié n'est pas un port possible (de 0 à 65535).")
            sys.exit(1)
        elif port <= 1024:
            print("ERROR: Le port spécifié est un port privilégié. Spécifiez un port au-dessus de 1024.")
            sys.exit(2)
        return port
    except ValueError:
        print("ERROR: Le port doit être un entier.")
        sys.exit(1)

parser = argparse.ArgumentParser(description="Serveur personnalisé")

parser.add_argument(
    '-p', '--port',
    type=check_port,
    default=13337,
    help="Spécifier un numéro de port (par défaut : 13337)"
)
args = parser.parse_args()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('10.1.1.10', args.port))
server_socket.listen(1)

logging.info(f"Serveur en attente de connexions sur l'adresse IP 10.1.1.10 et le port {args.port}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connexion établie avec {client_address}")
    client_socket.close()
