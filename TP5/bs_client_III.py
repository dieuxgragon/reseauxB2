import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.1.1.10', 13337))

# Récupération d'une string utilisateur
msg = input("Calcul à envoyer: ")

addition_count = msg.count('+')

if addition_count > 1:
    print("Erreur : Maximum de deux additions autorisées.")
else:
    msg_len = len(msg)
    payload = str(msg_len) + msg 


s.send(payload.encode())
# Réception et affichage du résultat
s_data = s.recv (4)
print(s_data.decode())
s.close()
