from ceasar_cipher import english_frequency

def repeating_key_xor(string, key):
    """
    both string and key must be in bytes format.
    """
    message = b''
    i = 0
    for char in string:
        message += bytes([char ^ key[i]])
        if i + 1 == len(key):
            i = 0
        else:
            i += 1

    return {
            'message': message,
            'score': english_frequency(message),
            'key': key
        }


if __name__ == '__main__':
    print(repeating_key_xor(input(), input()))
