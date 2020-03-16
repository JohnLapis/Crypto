import AES_ECB
from repeating_key_xor import repeating_key_xor


def encrypt(pt, key, iv):
    keysize = len(key)
    blocks = [pt[i:i+keysize] for i in range(0,len(pt),keysize)]
    ct = b''
    for block in blocks:
        xor = repeating_key_xor(block, iv)
        ecb = AES_ECB.decrypt(xor['message'], key)
        iv = ecb
        ct += ecb

    return ct

    
def decrypt(ct, key, iv):
    keysize = len(key)
    blocks = [ct[i:i+keysize] for i in range(0,len(ct),keysize)]
    pt = b''
    for block in blocks:
        ecb = AES_ECB.decrypt(block, key)
        xor = repeating_key_xor(ecb, iv)
        iv = block
        pt += xor['message']

    return pt


if __name__ == '__main__':
    with open('/home/john/Downloads/10.txt', 'r') as f:
        message = f.read().encode()#''.join([o[:-1] for o in f.readlines()]).encode()

    nt = decrypt(message, b'YELLOW SUBMARINE', b'\x00'*16)

    o = encrypt(nt, b'YELLOW SUBMARINE', b'\x00'*16)[:28]

