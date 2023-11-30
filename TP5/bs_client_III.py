import socket
import sys
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.1.1.10', 13337))
s.send('Hello'.encode())

# On reçoit la string Hello
data = s.recv(1024)

while True:
    msg = input("Calcul :")
    try:
        # Vérification si le nombre est inférieur ou égal à 4294967295
        num = int(msg)
        if 0 <= num <= 4294967295:
            break
        else:
            print("Nombre hors de la plage autorisée. Veuillez entrer un nombre entre 0 et 4294967295.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        
# Récupération d'une string utilisateur
msg = input("Calcul à envoyer: ")

# On envoie
s.send(msg.encode())

# Réception et affichage du résultat
s_data = s.recv(1024)
print(s_data.decode())
s.close()
