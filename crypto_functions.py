def shift_cypher(message, letters=None):
    if letters is None:
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message = message.upper()
    for key in range(len(letters)):
        translated = ''
        for symbol in message:
            if symbol in letters:
                num = letters.find(symbol)  # get the number of the symbol
                num = num - key
                if num < 0:
                    num = num + len(letters)
                translated = translated + letters[num]
            else:
                translated = translated + symbol
        print('Key #%s: %s' % (key, translated))


def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    while True:
        if((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater += 1
    return lcm


def L(a, n):
    return int((a - 1) / n)


def inverse_mod(a, m):
    g, x, y = euclidian_GCD(a, m)
    if g != 1:
        raise Exception('no inverse mod exists')
    else:
        return x % m


def euclidian_GCD(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = euclidian_GCD(b % a, a)
        return (g, y - (b // a) * x, x)
