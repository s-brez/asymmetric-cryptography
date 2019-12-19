def break_shift_cipher(message, letters=None):
    """Shift-by-n cipher breaker. Defaults to abx..xyz roman characters
    if no alphabet provided."""

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
    """ Return greatest common divisor of a and b."""

    if(b == 0):
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    """ Return lowest common multiple of a and b"""

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


def L(a, b):
    return int((a - 1) / b)


def euclidian_gcd(a, b):
    """ Return greatest common divisor of a and b."""

    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = euclidian_gcd(b % a, a)
        return (g, y - (b // a) * x, x)


def inverse_mod(a, b):
    """Return multiplicative modular inverse of a and b."""

    g, x, y = euclidian_gcd(a, b)
    if g != 1:
        raise Exception('No inverse mod exists')
    else:
        return x % b
