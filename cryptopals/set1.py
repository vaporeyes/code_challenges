from string import ascii_lowercase, ascii_uppercase
from base64 import b64encode
import re


# set 1
def hex2b64(s: str):
    return b64encode(bytes.fromhex(s))


# set 2
# 1c0111001f010100061a024b53535009181c
# 686974207468652062756c6c277320657965
def fixed_xor(x0, x1):
    if len(x0) != len(x1):
        return "Nope"
    return ''.join([x.split('x')[1] for x in [hex(int(x, 16) ^ int(y, 16)) for x, y in zip(x0, x1)]])


# set 3
def single_byte_xor(input_data: str):
    result = dict()
    high_score = 0
    freq = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u']
    keys = ascii_lowercase + ascii_uppercase
    for k in keys:
        output = ""
        cursor = 0
        while cursor < len(input_data):
            hx = input_data[cursor:cursor + 2]
            xor = int(hx, 16) ^ ord(k)
            output += str(xor)
            cursor += 2
        score = 0
        for i, key in enumerate(freq):
            pattern = re.compile(key)
            matches = pattern.match(output.lower())
            if matches:
                score += len(matches) * (12 - i)
        if score > high_score:
            high_score = score
            result[k] = output
    return result
