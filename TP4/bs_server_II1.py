import argparse
import sys

def check_port(value):
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

parser = argparse.ArgumentParser(description="Description de votre commande")

parser.add_argument(
    '-p', '--port',
    type=check_port,
    default=13337,
    help="Spécifier un numéro de port (par défaut : 13337)"
)
args = parser.parse_args()

print(f"Port spécifié : {args.port}")
