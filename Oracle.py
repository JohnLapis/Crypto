import os
import CBC as AES_CBC
import AES_ECB, PKSC7
from random import randint

def keygen(size):
    return os.urandom(size)

def encrypt(plain, keysize, choice):
    key = keygen(keysize)
    n = randint(5,10)
    m = randint(5,10)
    plain = (n * chr(n)).encode() + plain + (m * chr(m)).encode()

    if choice == 0:
        ct = AES_ECB.encrypt(PKSC7.main(plain, len(key)), key)
    else:
        ct = AES_CBC.encrypt(PKSC7.main(plain, len(key)), key, iv=os.urandom(16))

    return ct


def oracle(text, keysize, choice=randint(0,1)):
    text = b'a' * 48 + text
    cipher = encrypt(text, keysize, choice)
    blocks = [cipher[i: i + keysize] for i in range(0, len(cipher), keysize)]

    if blocks[1] == blocks[2]:
        return 'ECB'
    else:
        return 'CBC'
                             

if __name__ == '__main__':
#    with open('/home/john/Downloads/8.txt') as f:
#        texts = [c for c in f.read().split()]
    text = b'a' * 48
    print(oracle(text, 16))
