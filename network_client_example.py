from vlcb_server.network_client import VlcbClient
import asyncio


def process_message(msg):
    print(f'Process Message: {msg}')


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
