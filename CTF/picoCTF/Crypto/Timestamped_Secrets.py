from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

ciphertext = bytes.fromhex('24823b2b2d104b36ad2078cafc8d98f22488e78df83b29f507d9b910ad51a464')
timestamp = 1770242615

# Using the same 16-byte key generation logic
key = sha256(str(timestamp).encode()).digest()[:16]

# Decrypt using AES-128-ECB
cipher = AES.new(key, AES.MODE_ECB)
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

print(plaintext.decode())