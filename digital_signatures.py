import rsa
import elgamal


# RSA ################################################################

# message = 123456

# # sender generate keys
# keys = rsa.generate_keys(5563, 3821, 9623)
# print(keys)

# # sender generates message signature
# s = rsa.sign(keys['n'], keys['d'], message)
# print("Signature:", s)

# # receiver verifies the signiature and message
# verified = rsa.verify_signature(keys['n'], keys['e'], s, message)
# print("Message matches signature:", verified)

# ElGamal #############################################################

message = 4567

# sender generate keys
keys = elgamal.generate_keys(7331, 3411, 41)
print("Keys:", keys, "\n")

# sender chooses random int k, where 0 > k > p-1, and gcd(k, p-1) = 1
k = 919
print("Randomly chosen int k:", k)

# sender generates message signature
s = elgamal.sign(keys['g'], k, keys['p'], keys['x'], message)
print("Generated signature:", s)

# receiver verifies the signiature and message
verify = elgamal.verify_signature(
    keys['g'], keys['y'], keys['p'], s['r'], s['s'], message)
print(
    "\nVerification params v, w:", verify['v'], verify['w'],
    "\nMessage matches signature:", verify['result'])
