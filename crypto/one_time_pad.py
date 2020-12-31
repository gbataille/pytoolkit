import dataformats as df
from crypto import utils as crypto_utils


def cribdrag(
    enc1: bytes,
    enc2: bytes,
    crib: str,
    alphabet=set(
        'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,-_@!${}()[]^:;\'"<>? '
    ),
):
    """
    When you suspect that the same one time pad has been used to encrypt several strings, and you think you can guess
    part of a string content, you can use this method to try and find parts of the data and work your way from there
    """
    len_crib = len(crib)

    # Right padding
    if len(enc1) != len(enc2):
        # Make enc2 the small one
        if len(enc1) < len(enc2):
            temp = enc2
            enc2 = enc1
            enc1 = temp

        for _ in range(len(enc1) - len(enc2)):
            enc2 += b'\x00'

    xor = crypto_utils.xor_bytestrings(enc1, enc2)
    ialphabet = set(map(ord, list(alphabet)))
    for i in range(len(xor) - len_crib + 1):
        chunk = xor[i:i + len_crib]
        attempt = crypto_utils.xor_bytestrings(chunk, crib.encode())
        if all(map(lambda x: x in ialphabet, list(attempt))):
            print(
                f'found {attempt} with offset {i} and crib {crib} between {enc1} and {enc2}'
            )
