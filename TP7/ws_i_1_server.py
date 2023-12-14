import asyncio
import websockets

async def hello(websocket):
    name = await websocket.recv()
    print(f"<<< {name}")
    greeting = f"Hello client ! Received : {name}!"
    await websocket.send(greeting)
    print(f">>> {greeting}")

async def main():
    async with websockets.serve(hello, "10.1.2.10", 13337):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
