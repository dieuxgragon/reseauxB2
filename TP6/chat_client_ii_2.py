import socket
import aioconsole


async def async_input(writer):
    while True:
        msg = 'hello'.encode()
        writer.write(msg)
        await writer.drain()


        msg_client = await aioconsole.ainput()
        writer.write(msg_client.encode())
        await writer.drain()

async def async_received(reader):
        while True:
            data = await reader.read(1024)
            print(data.decode())

async def main():
    reader, writer = await asyncio.open_connection(host="10.1.1.10", port=13337)

    try:
         await asyncio.gather(async_input(writer), async_received(reader))
    except KeyboardInterrupt:
        pass
    finally:
         writer.close()
         await writer.close()

if __name__ == "__main__":
     asyncio.run(main())