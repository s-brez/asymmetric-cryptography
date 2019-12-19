import rsa
import hashlib
import crypto_functions as cf


# RSA text message signature scheme ##################################


message = "Cryptocurrencies continue to grow in price and size. Knowledge about Bitcoin, Litecoin, Ethereum, and others has spread through the entire world. Cryptocurrencies are providing such features and tools that simplify our lives. They are changing the way things work. Some people fear the changes. But changes are not always bad. Cryptocurrencies are modifying our lives, and the way industries develop. There’s no doubt that cryptocurrencies are disrupting and affecting the global economy in many ways."
print("Message:", message)

# Sender hashes the message then converts to decimal (from hex)
msg_hash = hashlib.md5(message.encode('utf-8')).hexdigest()
print("MD5 message Hash:", msg_hash)

msg_hash = int(msg_hash, 16)
print("Hash as decimal:", msg_hash)

# Sender generates keys
p = 278966591577398076867954212605012776073
q = 467207331195239613378791200749462989467
e = 41
keys = rsa.generate_keys(p, q, e)
print("Keys:", keys)

# Sender signs the message with the private key
# s = rsa.sign(keys['n'], keys['d'], msg_hash)

# Used wolfram alpha to find signature s = m^d mod n, python is way too slow
# for this operation.
s = 126798804286385130870848966135941566606057839336135951340495096277825470279796
print("Signature:", s)

# Receiver verifies the signature and message
verify = rsa.verify_signature(keys['n'], keys['e'], s, msg_hash)
print("Message matches signature:", verify)

# Receiver hashes the original message to check it matches the given hash
rehashed_msg = hashlib.md5(message.encode('utf-8')).hexdigest()
print("Re-hashed message:", rehashed_msg)
print(
    "Original message hash matches senders second hashing:", 
    int(rehashed_msg, 16) == msg_hash)
