from ceasar_cipher import ceasar
from binascii import unhexlify
import binascii

import locale


def main():
    with open('/home/john/Downloads/4.txt', 'r', encoding=locale.getpreferredencoding(False)) as f:
        n = 1
        possible_messages = []
        for line in f.readlines():
            try:
                d = ceasar(unhexlify(line[:-1].encode()))
                d['line'] = n
                possible_messages.append(d)
            except binascii.Error:
                d = ceasar(unhexlify(line.encode()))
                d['line'] = n
                possible_messages.append(d)
                
            n += 1
            

    best_message = sorted(possible_messages, key=lambda x: x['score'], reverse=True)[0]
    for item in best_message:
        print(item.title() + ':',  best_message.get(item))

    return best_message
    

if __name__ == '__main__':
    main()
