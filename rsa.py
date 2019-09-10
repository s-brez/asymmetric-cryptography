import crypto_functions as cf


def rsa_demo(p: int, q: int, e: int, message: int):
    """Demo's encryption and decryption with the given arguments."""
    print("RSA")

    # find public key param n
    n = p * q
    print("Message:", message)
    print("Primes p & q:", p, q)
    print("Public key parameter n: ", n)
    print("Public key parameter e: ", e)

    # find phi(n) and private key parameter d
    phi_n = (p - 1) * (q - 1)
    d = cf.inverse_mod(e, phi_n)
    print("Phi(n):", phi_n)
    print("Private key parameter d:", d, "\n")

    # keys
    print("Public key n, e:", n, e)
    print("Private key n, d:", n, d, "\n")

    # create ciphetext c = m**e % n
    c = message**e % n
    print("Ciphertext:", c)

    # decrypt c to verify plaintext m
    m = c**d % n
    print("Decrypted plaintext:", m)


def generate_keys(p: int, q: int, e: int):
    """ Return a dict containing private and public key parameters."""

    n = p * q
    d = cf.inverse_mod(e, (p - 1) * (q - 1))
    phi_n = (p - 1) * (q - 1)

    return {"n": n, "e": e, "d": d, "phi_n": phi_n}


def encrypt(n: int, e: int, m: int):
    """ Return encrypted ciphertext."""

    return m**e % n


def decrypt(n: int, d: int, c: int):
    """ Return decrypted plaintext."""

    return c**d % n


def sign(n: int, d: int, m: int):
    """ Return the signature for a given messsage."""

    return m**d % n


def verify_signature(n: int, e: int, s: int, m: int):
    """ Return true if signature matches message."""

    v = s**e % n
    print("Verfied m:", v)
    return v == m
