import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
s.send('Hello'.encode())

data = s.recv(1024)

while True:
    user_input = input("Calcul à envoyer: ")

    if len(user_input) <= 11:  

        parts = user_input.split()
        if len(parts) == 3 and parts[0].isdigit() and parts[2].isdigit() and parts[1] in ['+', '-', '*']:
            break
        else:
            print("Expression invalide. Veuillez entrer une expression arithmétique simple comme 'x opération y' (ex: 3 + 3).")
    else:
        print("Expression trop longue. Veuillez entrer une expression plus courte.")

s_data = s.recv(1024)
print(s_data.decode())
s.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 9999))

msg = input('Enter a message: ')

encoded_msg = msg.encode('utf-8')

msg_len = len(encoded_msg)

header = msg_len.to_bytes(4, byteorder='big')

payload = header + encoded_msg

sock.send(payload)
sock.close()
