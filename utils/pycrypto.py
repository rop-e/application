from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
from django.conf import settings

password = str(settings.SENHA_HASH).encode()


def encrypt(source):
    key = SHA256.new(password).digest()
    source = str(source).encode()
    IV = Random.new().read(AES.block_size)

    encryptor = AES.new(key, AES.MODE_CBC, IV)
    result = encryptor.encrypt(pad(source, AES.block_size))

    return b64encode(IV + result).decode()


def decrypt(source):
    key = SHA256.new(password).digest()
    source = b64decode(source.encode())
    IV = source[:AES.block_size]

    decryptor = AES.new(key, AES.MODE_CBC, IV)
    result = unpad(decryptor.decrypt(source[AES.block_size:]), AES.block_size)

    return bytes(result).decode()
