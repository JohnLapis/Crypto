from binascii import a2b_hex, b2a_base64

def hex_to_base64(hex_str):
    return b2a_base64(a2b_hex(hex_str), newline=False)

if __name__ == '__main__':
    hex_to_base64(input())
