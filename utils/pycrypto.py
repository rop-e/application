from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import base64


def encrypt(key, source, encode=True):
    key = SHA256.new(str(key).encode()).digest()
    IV = Random.new().read(AES.block_size)
    source = str(source).encode()

    encryptor = AES.new(key, AES.MODE_CBC, IV)
    padding = AES.block_size - len(source) % AES.block_size
    source += bytes([padding]) * padding

    data = IV + encryptor.encrypt(source)

    return base64.b64encode(data).decode() if encode else data


def decrypt(key, source, decode=True):
    if decode:
        source = base64.b64decode(source.encode())

    key = SHA256.new(str(key).encode()).digest()
    IV = source[:AES.block_size]

    decryptor = AES.new(key, AES.MODE_CBC, IV)
    data = decryptor.decrypt(source[AES.block_size:])
    padding = data[-1]

    if data[-padding:] != bytes([padding]) * padding:
        raise ValueError("Invalid padding...")

    return bytes(data[:-padding]).decode("utf-8")
