from secrets import token_bytes
from hashlib import sha256
from binascii import hexlify, unhexlify, a2b_base64, b2a_base64


def gen_32_byte_preimage():
    return token_bytes(32)


def bytes_to_hex(byte_string):
    return hexlify(byte_string)


def hex_to_bytes(hex_string):
    return unhexlify(hex_string)


def bytes_to_base64(byte_string):
    return b2a_base64(byte_string)


def base64_to_bytes(base64_string):
    return a2b_base64(base64_string)


def sha256_of_bytes_to_bytes(byte_string):
    return sha256(byte_string).digest()


def sha256_of_bytes_to_hex(byte_string):
    return sha256(byte_string).hexdigest()


def sha256_of_hex_to_hex(hex_string):
    byte_str = hex_to_bytes(hex_string)
    return sha256_of_bytes_to_hex(byte_str)