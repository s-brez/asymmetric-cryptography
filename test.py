import crypto_functions as cf

m = 5
x = 8
k = 9
p = 11
g = 2
r = g**k % p
k1 = cf.inverse_mod(k, p - 1)
val = k1 * (m - (x * r))

print(val)
