import json
import tomllib

# with open('vlcb_server/vlcb_message.json') as op_codes_file:
#     opcodes = json.load(op_codes_file)

with open("vlcb_message/vlcb_message.toml", "rb") as op_codes_filedes_toml_file:
    opcodes_toml = tomllib.load(op_codes_filedes_toml_file)


def get_str(msg, start, length):
    return msg[start: start + length]


def pad(num, length):
    output = '0000000000' + hex(num)[2:].upper()
    return output[length * -1:]


def get_int(msg, start, length):
    return int(msg[start: start + length], 16)


def node_id(msg):
    return int(get_str(msg, 9, 4), 16)


def opcode(msg):
    return get_str(msg, 7, 2)


def checkbit(number, bit):
    check_number = 1 << bit
    return number & check_number == check_number


def flags(flags):
    """
    Return dictionary of Parameter flags
    :param Single Byte integer:
    :return: Dictionary of standard parameters
    """
    # flags = int(input, 16)
    output = {}
    output['consumer'] = checkbit(flags, 0)
    output['producer'] = checkbit(flags, 1)
    output['flim'] = checkbit(flags, 2)
    output['bootloading'] = checkbit(flags, 3)
    output['coe'] = checkbit(flags, 4)
    output['learn'] = checkbit(flags, 5)
    output['vlcb'] = checkbit(flags, 6)
    return output

def process_bit_array(bit_array, value):
    pass

def replacer(s, newstring, index, length, nofail=False):
    # print(f'Replacing {index} with {newstring} in {s} {range(len(s))}')
    # raise an error if index is outside of the string
    if not nofail and (index > len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + length:]


def message_to_json(msg):
    if opcode(msg) not in opcodes_toml:
        print(f'CBUS Error op_code {opcode(msg)} not supported')
    else:
        output = {}
        for field, values in opcodes_toml[opcode(msg)].items():
            # print(f"opcode: {field}, values: {values}")
            if values[0] == ('str'):
                output[field] = get_str(msg, values[1], values[2])
                # print(f"{field} {get_str(msg, values['start'], values['length'])}")
            elif values[0] == 'int':
                output[field] = get_int(msg, values[1], values[2])
                # print(f"{field} {get_int(msg, values['start'], values['length'])}")
            elif values[0] == 'str-out':
                output[field] = get_str(msg, values[1], values[2])
            elif values[0] == 'str-json':
                output[field] = values[1]
            else:
                print(f"{field} Invalid Type : {values[0]}")
        # print(f"Grid to JSON TOML : {output}")
        return (output)


def json_to_message(json_msg):
    # print(f'opcode_details : {opcode_details}')
    # if json_msg['op_code'] not in opcodes_toml:
    #     print(f'opcode {opcode(json_msg)} not supported')
    #     return
    try:
        opcode_details = opcodes_toml[json_msg["op_code"]]
    except Exception as e:
        # print(f'Exception : {e}')
        return f'Exception : {e}'
    else:
        # opcode_details = opcodes_toml[json_msg["op_code"]]
        # Find the length on the message and check all required fields exist
        max_length = 0
        for field, values in opcodes_toml[json_msg["op_code"]].items():
            if values[0] in ['str', 'int']:
                length = values[1] + values[2]
                if length > max_length:
                    max_length = length
                if field not in json_msg:
                    return (f'{field} missing from json_msg : {json_msg}')

        vlcb_header = ':SB060N'
        vlcb_message = 'x' * (max_length - 7)
        vlcb_frame = vlcb_header + vlcb_message

        # print(f"Initial Message : {vlcb_frame}")
        for field, values in json_msg.items():
            field_details = opcode_details[field]
            # print(f'Field : {field} : {values} -- {field_details}')
            type = field_details[0]
            if type in ['str', 'int']:
                start = int(field_details[1])
                length = int(field_details[2])
                if type == 'str':
                    vlcb_frame = replacer(vlcb_frame, json_msg[field], start, length)
                elif type == 'int':
                    vlcb_frame = replacer(vlcb_frame, pad(json_msg[field], length) , start, length)
            elif type in ('str-out', 'str-json'):
                # print(f'Field not required : {field} : {values} -- {field_details}')
                pass
            else:
                print(f'JSON ERROR:{field} : {values} {field_details}')
        print(f'output JSON to Grid: {vlcb_frame}')
        # display_opcode_details(op_code)
    return vlcb_frame

def display_opcode_details(op_code):
    print(f'Required Fields for op_code: {op_code}')
    for field, values in opcodes_toml[op_code].items():
        if values[0] in ['str', 'int']:
            print(f"Required Fields: {field} : {values}")


# def get_opcode_required_fields(op_code):
#     required_fields = []
#     for field, values in opcodes_toml[op_code].items():
#         if values[0] in ['str', 'int']:
#             required_fields.append(values)
#     return required_fields
