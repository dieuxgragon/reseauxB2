import asyncio
import websockets

async def hello(websocket):
    name = await websocket.recv()
    print(f"<<< {name}")
    greeting = f"Hello {name}!"
    await websocket.send(greeting)
    print(f">>> {greeting}")


    while True:
        msg = await websocket.recv()
        print(f"<<< {msg}")
        rsp = f"MSG received {name}!"
        await websocket.send(rsp)
        print(f"{rsp}")

async def main():
    async with websockets.serve(hello, "10.1.2.10", 13337):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
