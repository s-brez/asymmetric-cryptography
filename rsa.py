import crypto_functions as cf


def rsa(p: int, q: int, e: int, message: int):

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
