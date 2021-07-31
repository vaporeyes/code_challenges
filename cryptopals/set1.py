from base64 import b64encode

def hex2b64(s: str):
    return b64encode(bytes.fromhex(s))
