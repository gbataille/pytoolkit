def string_to_int(string: str) -> int:
    return int(string.encode().hex(), 16)


def bytes_to_int(b: bytes) -> int:
    return int(b.hex(), 16)


def int_to_bytes(number: int) -> bytes:
    return hex_to_bytes(hex(number))


def hex_to_bytes(hex_string: str) -> bytes:
    if hex_string.startswith('0x'):
        hex_string = hex_string[2:]

    if len(hex_string) % 2 != 0:
        hex_string = '0' + hex_string

    return bytes.fromhex(hex_string)


def hex_to_string(hex_string: str) -> str:
    bstring = hex_to_bytes(hex_string)
    return bstring.decode()


def int_to_string(number: int) -> str:
    bstring = int_to_bytes(number)
    return bstring.decode()
