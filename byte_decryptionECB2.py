from AES_ECB import encrypt
from random import randint
import os, re
#from Oracle import oracle dat shit wrong
from PKSC7 import main as PKSC7

key = os.urandom(16)
keysizes = [16, 24, 32]

def encryp(text, plain, key):
    return encrypt(PKSC7(plain + text, len(key)), key)

def getBlockSize(text):
    plain = b''
    size1 = len(encryp(text, plain, key))
    plain += b'a'
    size2 = len(encryp(text, plain, key))

    while size1 == size2:
        plain += b'a'
        size2 = len(encryp(text, plain, key))
    return size2 - size1


def getPlainSize(text):
    plain = b''
    emptyCt = len(encryp(text, plain, key))
    
    maxCt = emptyCt - 1
    while True:
        plain += b'a'
        newCt = len(encryp(text, plain, key))
        if newCt == emptyCt:
            maxCt -= 1
        else:
            return maxCt


def getNextByte(offset, cipher, blockSize, text):
    plain = b'a' * (blockSize - 1 - len(offset))
    for i in range(256):
        newPlain = plain + chr(i).encode()
        newCipher = encryp(text, newPlain, key)
        a = newCipher[0:blockSize]
        b = cipher[0:blockSize]
        print(text)
        print('----------')
        print(newPlain)
        print()
        if a == b:
            return chr(i).encode()
        
def getPlain(text):
    blockSize = getBlockSize(text)
    plainSize = getPlainSize(text)
    known = b''
    for i in range(plainSize):
        padSize = blockSize - 1 - (len(known) % blockSize)
        pad = b'a' * padSize
        cipher = encryp(text, pad, key)
        cipherChuncks = [cipher[i:i+blockSize] for i in range(0,len(cipher),blockSize)]
        cipherOfInterest = cipherChuncks[len(known) // 16]
        offset = (pad + known)[-15:]
        known += getNextByte(offset, cipherOfInterest, blockSize, text)

    return known


if __name__ == '__main__':
    from binascii import a2b_base64
    
    unknown = a2b_base64('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')

    print("Block size:", getBlockSize(unknown))
    print("Mode:", oracle(unknown, len(key), 0))
    print(PKSC7(unknown, len(key)))
    #print("Plaintext:", getPlain(unknown))

