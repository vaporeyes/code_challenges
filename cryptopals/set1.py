def hex2b64(h):
    """
    convert hex to base64
    """
    return h.decode("hex").encode("base64")

def xor_byte_strings(s1, s2):
    s1 = bytes.fromhex(s1)
    s2 = bytes.fromhex(s2)
    return bytes([a ^ b for a,b in zip(s1, s2)]).hex()