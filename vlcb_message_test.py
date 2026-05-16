from vlcb_message import message_to_json
from vlcb_message import json_to_message
from vlcb_server import VlcbClient
import asyncio


def process_message(msg):
    # print(f'Process Message: {msg}')
    cbus_message = message_to_json(msg)
    grid_connect_string = json_to_message(cbus_message)
    if grid_connect_string[6:] == msg[6:]:
        print(f'{cbus_message['status']} :: {msg} - {cbus_message['description']}- {grid_connect_string}')
    else:
        print(f'ERROR :: {msg} -- {grid_connect_string} :: {cbus_message['op_code']} -- {cbus_message['description']}')

async def main(name: str) -> None:
    cbus_header = ':SB060N'
    VLCB_client = VlcbClient(process_message, "localhost", 5550)
    asyncio.create_task(VLCB_client.run())
    VLCB_client.send(f'{cbus_header}0D;')
    while True:
        await asyncio.sleep(0.01)


if __name__ == '__main__':
    # main('network Client')
    asyncio.run(main('Network Client Example'))
