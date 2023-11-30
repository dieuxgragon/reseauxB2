import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.1.1.10', 9999))
s.send('Hello'.encode())

data = s.recv(1024)

msg = input("Calcul à envoyer: ")

s.send(msg.encode())

s_data = s.recv(1024)
print(s_data.decode())
s.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('10.1.2.10', 9999))

msg = input('Enter a message: ')

encoded_msg = msg.encode('utf-8')

msg_len = len(encoded_msg)

header = msg_len.to_bytes(4, byteorder='big')

payload = header + encoded_msg

sock.send(payload)
sock.close()
