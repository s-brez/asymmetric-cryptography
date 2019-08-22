import crypto_functions as cf
import paillier


# vote counter
votes = "0000"

# candidate a voting messages
vm_a = "0100"
vm_b = "0001"

# VA generates public key (n, g) and private key (ƛ, μ)
paillier.paillier(5, 7, 4, 164, 6)
