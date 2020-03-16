def pad_validation(string):
    last_byte = chr(string[-1]).encode()
    #because bytes turn into numbers when indexed
    supposed_padding = last_byte * ord(last_byte)

    if supposed_padding == string[-ord(last_byte):]:
        return string[:-ord(last_byte)]
    else:
        raise Exception('Invalid padding.')
        

if __name__ == '__main__':
    print(pad_validation(b'sdfa' + 4*chr(3).encode()))
