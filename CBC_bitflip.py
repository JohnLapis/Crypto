import CBC as AES_CBC
from PKSC7 import main as PKSC7
import re, os


key = os.urandom(16)
iv = os.urandom(16)

def encrypt(pt):
    s1 = b'comment1=cooking%20MCs;userdata='
    s2 = b';comment2=%20like%20a%20pound%20of%20bacon'
    pt = re.sub(b';|=', b'', pt) #quote out metacharacters
    pt = s1 + pt + s2
    pt = PKSC7(pt, len(key))
    return AES_CBC.encrypt(pt, key, iv)

    
def decrypt(ct):
    pt = AES_CBC.decrypt(ct, key, iv)
    print(pt, len(pt))
    if re.search(b';admin=true;', pt):
        return True
    else:
        return False


def modCipher(ct):
    """
    Modify the ciphertext to get ';admin=true;'
    out of the decryptor without knowing the key
    """
    target_bytes = ct[16: len('a;admin=true;')+16]
    try:
        print(re.search(target_bytes,ct))
    except:
        print()
    
    new_bytes = b''.join([bytes([b ^ 1]) for b in target_bytes])
    ct = re.sub(r'{}'.format(target_bytes), new_bytes, ct, 1)
    return ct

    
if __name__ == '__main__':
    pt = b''.join([bytes([ord(c) ^ 1]) for c in 'a;admin=true;'])
    print(decrypt(encrypt(pt)))
    print(decrypt(modCipher(encrypt(pt))))
