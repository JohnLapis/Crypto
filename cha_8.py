from binascii import a2b_hex
import AES_ECB, ceasar_cipher


def rep_blocks(l, keysize):
    blocks = [l[i:i+keysize] for i in range(0,len(l),keysize)]
    return len(blocks) - len(set(blocks))

def main(cts):
    keysize = 16
    for i in range(len(cts)):
        cts[i] = rep_blocks(cts[i], keysize), cts[i]

    most_reps = sorted(cts, key=lambda x: x[0], reverse=True)[0]
    
    return most_reps


if __name__ == '__main__':
    with open('/home/john/Downloads/8.txt', 'r') as f:
        ciphertexts = [a2b_hex(o) for o in f.read().split()]

    print(main(ciphertexts))
