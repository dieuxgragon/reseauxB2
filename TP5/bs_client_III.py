import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.1.1.10', 13337))

# Récupération d'une string utilisateur
msg = input("Calcul à envoyer: ")

msg_len = len(msg)
if msg_len > 3:
    print("calcule trop long essaye a + b")
    SystemExit

payload = str(msg_len) + msg 


s.send(payload.encode())
# Réception et affichage du résultat
s_data = s.recv (4)
print(s_data.decode())
s.close()
