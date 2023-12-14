import asyncio
import websockets

async def hello():
    uri = "ws://10.1.2.10:13337"
    async with websockets.connect(uri) as websocket:
            name = input("What's your name ? ")

            await websocket.send(name)
            print(f">>> {name}")

            greeting = await websocket.recv()
            print(f"<<< {greeting}")

    while True:
         msg = input("Send your Text : ")

         await  websocket.send(msg)
         print (f">>> {name} :")

         rsp = await websocket.recv()
         print(f"<<< {rsp}")

if __name__ == "__main__":
    asyncio.run(hello())
