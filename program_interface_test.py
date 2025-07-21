from vlcb_server.network_client import VlcbClient

from vlcb_server.vlcb_message import message_to_json
from vlcb_server.vlcb_message import json_to_message

import asyncio


def process_message(msg):
    json_output = message_to_json(msg)
    print(f'Message to JSON : {json_output}')
    message_output = json_to_message(json_output)
    print(f'JSON to Message : {message_output}')

async def main(name: str) -> None:
    cbus_header = ':SB060N'
    VLCB_client = VlcbClient(process_message, "localhost", 5550)
    asyncio.create_task(VLCB_client.run())
    VLCB_client.send(f'{cbus_header}0D;')
    while True:
        await asyncio.sleep(1)


if __name__ == '__main__':
    # main('network Client')
    asyncio.run(main('Network Client Example'))
