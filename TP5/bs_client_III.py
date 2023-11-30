import socket

while True:
    try:
        msg = input()
        # Vérification si le nombre est inférieur ou égal à 4294967295
        if int(msg) > 4294967295:
            print("Nombre trop grand. Veuillez entrer un nombre inférieur ou égal à 4294967295.")
        else:
            break
    except ValueError:
        print("Veuillez entrer un nombre valide.")
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.1.1.10', 13337))
s.send('Hello'.encode())

# On reçoit la string Hello
data = s.recv(1024)

# Récupération d'une string utilisateur
msg = input("Calcul à envoyer: ")

# On envoie
s.send(msg.encode())

# Réception et affichage du résultat
s_data = s.recv(1024)
print(s_data.decode())
s.close()
