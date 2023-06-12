#!/usr/bin/env python3
import asyncio

async def handle_client(reader, writer):
    while True:
        data = await reader.read(1024)
        if not data:
            break
        message = data.decode().strip()
        print(f"Received message: {message}")
        # Process the received message here

    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, '0.0.0.0', 12345)
    print("Server started. Listening on 0.0.0.0:12345")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
