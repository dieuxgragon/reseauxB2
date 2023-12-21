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
        print(f"taille du message {msg_len}")

        if not msg_len:
            break
        intmsg = int.from_bytes(msg_len, 'little') 
        print(intmsg) 
        msg = conn.recv(intmsg)
        print(f"le message = {msg}")

        # Evaluation et envoi du résultat
        res = eval(msg.decode())
        conn.send(str(res).encode())
         
    except socket.error:
        print("Error Occured.")
        break

conn.close()
