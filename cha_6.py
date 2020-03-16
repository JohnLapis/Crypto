from binascii import a2b_base64 #temp
import binascii
import locale
from repeating_key_xor import repeating_key_xor
from ceasar_cipher import ceasar


def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        return

    dist = 0
    s1 = s1.encode()
    s2 = s2.encode()
    
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            dist += bin(s1[i] ^ s2[i]).count("1")
            
    return dist


def key_generator_broken(keysize):
    """256 to the power of keysize"""
    key = chr(0) * keysize
    i = len(key) - 1
    while key != chr(256) * keysize:
        yield key
        key[i] = chr(ord(key[i]) + 1)
        
        j = len(key) - 1
        for c in reverse(key):
            if ord(c) == 256:
                c = chr(0)
                j -= 1
            elif key[j] == c:
                key[j] = chr(ord(key[j]) + 1)
                continue

            
def decrypt(string):
    probable_keysizes = []

    """
    Calculating the hamming distance between to fragments of the string
    for each key size
    """
    
    for keysize in range(2,40):
        hdistance = 0
        keysizes = {}
        if len(lines) / 2 < keysize:
            break
        
        for i in range(0, len(string), keysize*2):
            a = hamming_distance(string[i : i+keysize], string[i+keysize : i+keysize*2])

            if type(a) != int:
                break

            hdistance += a

        keysizes['size'] = keysize
        keysizes['dist'] = hdistance
        probable_keysizes.append(keysizes)

    #taking the keysize from the smallest hamming distance
    keysize = sorted(probable_keysizes, key=lambda x: x['dist'])[0]['size']
    #print([(i['size'], i['dist']) for i in keysize])
    #braking the string into blocks of keysize size

    blocks = [string[i::keysize] for i in range(keysize)]

    key = ''
    for block in blocks:
        key += chr(ceasar(block.encode())['shift'])

    message = repeating_key_xor(string, key)
    print(len(key))
    return message
    
        
if __name__ == '__main__':
    f = open('/home/john/Downloads/6.txt', 'r',
             encoding=locale.getpreferredencoding(False))
    lines = ''.join([a2b_base64(line[:-1].encode()).decode() for line in f.readlines()])
    f.close()
    print(decrypt(lines))
