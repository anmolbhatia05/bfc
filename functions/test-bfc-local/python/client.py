#!/usr/bin/env python3
import time
import random
import asyncio
from socket import *
from click import command, option, Choice
from socksx.socks6 import Client
from socksx.socket import SocketAddress

@command()
@option('-d', '--debug', default=False, help="Prints debug information")
@option('-d', '--destination', default="127.0.0.1:12345", help="Address of the destination")
@option('-p', '--proxy', default='127.0.0.1:1080', help="Address of the proxy")
@option('-s', '--socks', default=6, type=Choice([6]), help="SOCKS version")
def cli(**kwargs):
    print("here")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop, **kwargs))

async def main(loop, debug, destination, proxy, socks):
    """

    """
    # --debug  and --socks are currently ignored.
    destination = SocketAddress(destination)

    client = Client(proxy)
    try:
        socket = await client.connect(destination)
        # raw_fd = await socket.get_raw_fd()
        # print(f"RAW SOCKET FD: {raw_fd}")
        # py_socket = fromfd(raw_fd, AF_PACKET, SOCK_RAW)
        # print(py_socket)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    cli()
