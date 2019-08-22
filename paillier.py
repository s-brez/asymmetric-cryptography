import crypto_functions as cf


def paillier(p: int, q: int, m: int, g: int, r: int):

    print("Paillier")

    # find public key param n
    n = p * q
    print("Message m:", m)
    print("Primes p & q:", p, q)
    print("Public key parameter n:", n)
    print("Public key parameter g:", g)

    # find private key params (ƛ, μ)
    ƛ = cf.lcm(p - 1, q - 1)
    k = cf.L((g**ƛ) % (n**2), n)
    μ = cf.inverse_mod(k, n)
    print("Private key parameter ƛ:", ƛ)
    print("Pre-parameter k:", k)
    print("Private key parameter μ:", μ, "\n")

    # keys
    print("Public key (n, g):", n, g)
    print("Private key (ƛ, μ):", ƛ, μ, "\n")

    # find ciphertext c = g**m r**n mod n**2
    c = g**m * r**n % n**2
    print("Ciphertext:", c)

    # decrpyt c to verify the plaintext m
    p = cf.L(c**ƛ % n**2, n) * μ % n
    print("Decrypted plaintext:", p)


def keys_only():
    
