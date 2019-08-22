import crypto_functions as cf
import paillier

COUNTER_SIZE = 8

# determine voting messages by evaluating the splitting of 
# a COUNTER_SIZE length string of bits: 001001 						
# candidates voting messages:		      ^  ^
vm_a = 16 # binary 16 as int
vm_b = 1 # binary 1 as int

# VA generates public key (n, g) and private key (ƛ, μ)
keys = paillier.keys(641, 1019, 173)
print("Keys:", keys)

# votes cast their votes, with int r randomly chosen by each voter
# a vote of "1" is candidate B, vote of "4" is candidate A
v1 = (paillier.encrypt(keys['n'], keys['g'], 6, vm_a))
v2 = (paillier.encrypt(keys['n'], keys['g'], 31, vm_b))
v3 = (paillier.encrypt(keys['n'], keys['g'], 17, vm_b))
v4 = (paillier.encrypt(keys['n'], keys['g'], 22, vm_a))
v5 = (paillier.encrypt(keys['n'], keys['g'], 11, vm_a))
v6 = (paillier.encrypt(keys['n'], keys['g'], 8, vm_a))
v7 = (paillier.encrypt(keys['n'], keys['g'], 19, vm_b))
v8 = (paillier.encrypt(keys['n'], keys['g'], 29, vm_a))
v9 = (paillier.encrypt(keys['n'], keys['g'], 31, vm_b))

# tally the votes utilising pailliers homomorphic addition property
# multiply all ciphertexts then mod n**2
print("Votes plaintext:", v1, v2, v3, v4, v5, v6 ,v7, v8, v9)

ciphertext_total = (v1 * v2 * v3 * v4 * v5 * v6 * v7 * v8 * v9) % keys['n']**2
print("Totalled votes (c):", ciphertext_total)

# now VA decrypts the total
plaintext_total = paillier.decrypt(keys['ƛ'], keys['μ'], keys['n'], ciphertext_total)

# convert plaintext to binary and slice off the python "0b" prefix
binary_total = bin(plaintext_total)[2:]

# account for missing zeros, will happen if theres a low amount of voters
diff = COUNTER_SIZE - (len(binary_total))
if diff != 0:
	binary_total = "0" * diff + binary_total
print("Binary total:", binary_total)

# split the bits in half
split = int(COUNTER_SIZE / 2)
candidate_a_votes = binary_total[:split]
candidate_b_votes = binary_total[-split:]

# convert split binary words back to decimal
candidate_a_votes = int(candidate_a_votes, 2)
candidate_b_votes = int(candidate_b_votes, 2)

print(
	"Candidate A total votes:", candidate_a_votes,
	"\nCandidate B total votes:", candidate_b_votes)