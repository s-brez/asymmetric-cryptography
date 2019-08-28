import crypto_functions as cf


def elgamal_demo(p: int, g: int, x: int, r: int, message: int):
    """Demo's encryption and decryption with the given arguments."""

    print("ElGamal")

    # find public key parameter y
    y = g**x % p
    print("Message:", message)
    print("Prime p:", p)
    print("Generator g:", g)
    print("Randomly chosen int r:", r)
    print("Public key parameter y:", y, "\n")

    # keys
    print("Public key y, g, p:", y, g, p)
    print("Private key x:", x, "\n")

    # find k
    k = y**r % p
    print("Parameter k:", k, "\n")

    # encrypt m to find c1 and c2
    c1 = g**r % p
    c2 = message * k % p
    print("Ciphertext c1:", c1)
    print("Ciphertext c2:", c2, "\n")

    # decrypt c1 and c2 to derive k and k1
    d_k = c1**x % p
    k1 = cf.inverse_mod(k, p)
    print("Derived parameter k:", d_k)
    print("Parameter k1:", k1, "\n")

    # decrypt c1 and c2 to verify m
    m = k1 * c2 % p
    print("Decrypted plaintext:", m, "\n")


def generate_keys(p: int, g: int, x: int):
    """ Return a dict containing private and public key parameters."""

    y = g**x % p

    return {"p": p, "g": g, "y": y, "x": x}


def sign(g: int, k: int, p: int, x: int, m: int):
    """ Return the signature parameters for a given messsage."""

    r = g**k % p
    k1 = cf.inverse_mod(k, p - 1)
    val = k1 * (m - (x * r))
    s = val % (p - 1)
    return {"r": r, "s": s}


def verify_signature(g: int, y: int, p: int, r: int, s: int, m: int):
    """ Return verification params and boolean result."""

    v = g**m % p
    w = ((y**r) * (r**s)) % p
    return {"result": v == w, "v": v, "w": w}
