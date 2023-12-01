import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('10.1.1.10', 13337))  

s.listen(1)
conn, addr = s.accept()

while True:

    try:
        # On reçoit le calcul du client
        msg_len = conn.recv(1)

        print(msg_len)

        intmsg = int.from_bytes(msg_len, byteorder='little')   
        msg = conn.recv(intmsg)

        print(msg)
        print(type(msg))

        # Evaluation et envoi du résultat
        res  = eval(msg.decode())
        conn.send(str(res).encode())
         
    except socket.error:
        print("Error Occured.")
        break

conn.close()
