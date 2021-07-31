from base64 import b64encode


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
