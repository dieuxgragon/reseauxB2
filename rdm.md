serveur 


    while True:
        msg = await websocket.recv()
        print(f"<<< {msg}")
        rsp = f"MSG received {name}!"
        await websocket.send(rsp)
        print(f"{rsp}")


client
    while True:
         msg = input("Send your Text : ")

         await  websocket.send(msg)
         print (f">>> {name} :")

         rsp = await websocket.recv()
         print(f"<<< {rsp}")