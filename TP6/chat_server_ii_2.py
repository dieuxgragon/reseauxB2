import asyncio

async def handle_client_msg(reader, writer):
    while True:

        data = await reader.read(1024)
        addr = writer.get_extra_info('peername')

        if data == b'':
            break
        
        if addr not in clients:
            clients[addr] = {}
            clients[addr]["r"] = reader
            clients[addr]["w"] = writer

            
        writer.write(f"Hello {addr[0]} : {addr[1]}".encode())
        await writer.drain()

        message = data.decode()
        print(f"Message Received From {addr[0]} : {addr[1]} : {message}")

async def main():
    global clients
    clients = {}
    server = await asyncio.start_server(handle_client_msg, '10.1.1.10', 13337)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())