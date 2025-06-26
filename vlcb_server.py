from vlcb_server.server import VLCBServer
from vlcb_server.canusb4 import CanUsb4
import asyncio
import time
import serial.tools.list_ports as list_ports

HOST = '127.0.0.1'
PORT = 5550
# USB_PORT = '/dev/cu.usbmodem214101'
# canusb4s = []


async def main():
    server = VLCBServer(HOST, PORT)
    asyncio.create_task(server.start_server())

    await asyncio.sleep(1)

    for port in list(list_ports.comports()):
        port_name = str(port[2])[12:21]
        print(f"Found {str(port[0])}")
        if port_name.upper() == '04D8:F80C':
            print(f'Found USB4 {str(port[0])}')
            usb_port = str(port[0])
            canusb4 = CanUsb4(usb_port, HOST, PORT)

            asyncio.create_task(canusb4.messages_from_usb())
            asyncio.create_task(canusb4.messages_from_server())

    while True:
        await asyncio.sleep(0.0001)

if __name__ == "__main__":
    asyncio.run(main())

