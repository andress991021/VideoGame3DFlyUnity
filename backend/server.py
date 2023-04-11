#!/usr/bin/env python

import asyncio
from websockets.server import serve
from settings import settings

async def echo(websocket):
    async for message in websocket:
        print(message)
        #msg = random.choice(["A", "B","C"])
        #await websocket.send(msg)

async def main():
    async with serve(echo, settings.host, settings.port):
        await asyncio.Future()  # run forever

asyncio.run(main())