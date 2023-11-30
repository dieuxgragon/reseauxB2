import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.1.1.10', 13337))
s.send('Hello'.encode())

# On reçoit la string Hello
data = s.recv(1024)

# Récupération d'une string utilisateur
msg = input("Calcul à envoyer: ")
while True:
    user_input = input("Calcul à envoyer: ")
    # Vérification de la longueur de l'expression
    if len(user_input) <= 11:  # Longueur maximale de 11 caractères pour "4294967295"
        # Vérification si l'expression est valide
        parts = user_input.split()
        if len(parts) == 3 and parts[0].isdigit() and parts[2].isdigit() and parts[1] in ['+', '-', '*']:
            break
        else:
            print("Expression invalide. Veuillez entrer une expression arithmétique simple comme 'x opération y' (ex: 3 + 3).")
    else:
        print("Expression trop longue. Veuillez entrer une expression plus courte.")

# On envoie
s.send(msg.encode())

# Réception et affichage du résultat
s_data = s.recv(1024)
print(s_data.decode())
s.close()
