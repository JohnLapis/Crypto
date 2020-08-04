from binascii import a2b_base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


def decrypt(ct, key):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()
    return decryptor.update(ct) + decryptor.finalize()

def encrypt(pt, key):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()
    return encryptor.update(pt) + encryptor.finalize()


if __name__ == '__main__':
    with open('7.txt', 'r') as f:
        message = a2b_base64(f.read().encode())

    key = b'YELLOW SUBMARINE'
    print(decrypt(message, key))
