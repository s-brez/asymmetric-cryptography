import rsa
import hashlib
import crypto_functions as cf


# RSA text message signature scheme ##################################

# message = "Cryptocurrencies continue to grow in price and size. Knowledge about Bitcoin, Litecoin, Ethereum, and others has spread through the entire world. Cryptocurrencies are providing such features and tools that simplify our lives. They are changing the way things work. Some people fear the changes. But changes are not always bad. Cryptocurrencies are modifying our lives, and the way industries develop. There’s no doubt that cryptocurrencies are disrupting and affecting the global economy in many ways."
message = "Security in Computing 2018"
print("Message:", message)

# Sender hashes the message then converts to decimal (from hex)
# msg_hash = hashlib.md5(message.encode('utf-8')).hexdigest()
msg_hash = "db1623867ac43b924848c0bc81a6e689"
print("MD5 Hash:", msg_hash)

msg_hash = int(msg_hash, 16)
print("As decimal:", msg_hash)

# Sender generates keys
p = 335011793073035265521070150212791157303
q = 185296104977565236504132463330798131651
e = 5737
keys = rsa.generate_keys(p, q, e)
print("Keys:", keys)

# Sender signs the message with the private key
s = rsa.sign(keys['n'], keys['d'], msg_hash)
print("Signature:", s)

# receiver verifies the signature and message
verified = rsa.verify_signature(keys['n'], keys['e'], s, msg_hash)
print("Message matches signature:", verified)

# Receiver hashes the original message to check it matches the given hash 