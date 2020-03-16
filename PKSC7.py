from cryptography.hazmat.primitives import padding
import AES_ECB

def main(text, keysize):
    padder = padding.PKCS7(keysize * 8).padder()
    padded_text = padder.update(text) + padder.finalize()
    return padded_text


if __name__ == '__main__':
    from binascii import a2b_base64
    
    with open('/home/john/Downloads/7.txt', 'r') as f:
        text = f.read()[:60].encode()


    key = b'YELLOW SUBMARINE'
    
    try:
        print(len(text) % len(key))
        print(main(text, len(key)))
        print('ok')
    except ValueError:
        text = main(text, len(key))
        print(len(text) % len(key))
        AES_ECB.main(text, len(key))
        print('ok')
