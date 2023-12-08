import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.1.2.10', 13337))

s.send(b"hello")

data = s.recv(1024)
print("receive :", data.decode())

