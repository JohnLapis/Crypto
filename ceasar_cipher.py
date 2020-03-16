#import quotes_spider

def english_frequency(message):
    frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }

    return sum([frequencies.get(c, 0) for c in message])


def best_message(potential_messages):
    return sorted(potential_messages, key=lambda x: x['score'], reverse=True)[0]


def ceasar(code):
    potential_messages = []
    for i in range(256):
        message = ''.join([chr(o ^ i) for o in code])
        potential_messages.append({
            'message': message,
            'score': english_frequency(message),
            'shift': i
        })

    message = best_message(potential_messages)
    
    return message

        
if __name__ == '__main__':
    ceasar(input())
