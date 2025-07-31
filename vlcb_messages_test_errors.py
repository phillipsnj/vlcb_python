
from vlcb_server.vlcb_message import message_to_json
from vlcb_server.vlcb_message import json_to_message



# def process_message(msg):
#     json_output = message_to_json(msg)
#     print(f'Message to JSON : {json_output}')
#     message_output = json_to_message(json_output)
#     print(f'JSON to Message : {message_output}')

def main(name: str) -> None:
    cbus_header = ':SB060N'

    vlcb_msg = cbus_header + '98012C0009'
    print(f'Invalid Op Code - {vlcb_msg} {message_to_json(vlcb_msg)}')
    print()
    vlcb_msg = cbus_header + '90012CA5'
    print(f'Invalid Length - {message_to_json(vlcb_msg)}')
    print()
    json_msg = {'opcode': '91', 'node_number': 300, 'event_number': 15}
    print(f'Invalid JSON  - {json_to_message(json_msg)}')
    print()
    json_msg = {'op_code': '91', 'node_number': 300, 'eventnumber': 15}
    print(f'Missing JSON Field   - {json_to_message(json_msg)}')
    print()


if __name__ == '__main__':
    main('network Client')

