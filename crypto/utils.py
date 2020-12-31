def xor_strings(s1: str, s2: str) -> bytes:
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(s1, s2))
