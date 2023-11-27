import argparse
import socket

def check_port(value):
    try:
        port = int(value)
        if port < 0 or port > 65535:
            raise argparse.ArgumentTypeError("Le port spécifié n'est pas un port possible (de 0 à 65535).")
        elif port <= 1024:
            raise argparse.ArgumentTypeError("Le port spécifié est un port privilégié. Spécifiez un port au-dessus de 1024.")
        return port
    except ValueError:
        raise argparse.ArgumentTypeError("Le port doit être un entier.")

parser = argparse.ArgumentParser(description="Description de votre commande")

parser.add_argument(
    '-p', '--port',
    type=check_port,
    default=13337,
    help="Spécifier un numéro de port (par défaut : 13337)"
)

args = parser.parse_args()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('10.1.2.10', args.port))
server_socket.listen(1)

print(f"Serveur en attente de connexions sur le port {args.port} depuis l'adresse IP 10.1.2.10")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connexion établie avec {client_address}")
    client_socket.close()
