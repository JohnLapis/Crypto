from pprint import pprint
import re,json


def parser(exp=None, kexp=9):
    if exp == None:
        encoded = []
        for i in range(len(kexp)):
            encoded.insert(0, '='.join(kexp.popitem()))
        return '&'.join(encoded)
    else:
        d = [] #will be a dictionary
        for pair in exp.split('&'):
            d.append(tuple(pair.split('=')))

    return parser(kexp=dict(d))


uid = 0
def profile_for(email):
    if '=' in email or '&' in email:
        print("'=' and '&' are invalid characters.")
        return
    return parser(
        'email='+email +
        '&uid='+str(uid) +
        '&role=user'
    )


if __name__ == '__main__':
    print(profile_for('foo@bar.com'))
