Someone encrypted a message using AES in ECB mode but they weren’t very careful with their key.  
Turns out it’s derived from something as simple as the current time!  
Can you uncover the key and decrypt the flag?  

[encryption.py](https://github.com/user-attachments/files/30419131/encryption.py)
from hashlib import sha256
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def encrypt(plaintext: str, timestamp: int) -> str:
    timestamp = int(time.time())
    key = sha256(str(timestamp).encode()).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded)
    return ciphertext.hex()

if __name__ == "__main__":
  
    plaintext = "picoCTF{...}"
    result = encrypt(plaintext, key)
    print(f"Hint: The encryption was done around {timestamp} UTC\n")
    print(f"Ciphertext (hex): {ciphertext.hex()}\n")


This is an AES-ECB encryption algorithm python code.  
The key is generated using a timestamp


[message.txt](https://github.com/user-attachments/files/30418662/message.txt)

Hint: The encryption was done around 1770242615 UTC
Ciphertext (hex): 24823b2b2d104b36ad2078cafc8d98f22488e78df83b29f507d9b910ad51a464

Since the hint provides the ciphertext in hex format and the timestamp,  
the timestamp can be subbed in to decode the ciphertext using same algorithm in encryption.py

[Timestamped_Secrets.py](https://github.com/user-attachments/files/30419167/Timestamped_Secrets.py)
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

Flag: picoCTF{sa3S_sEc9t_fbbd0fb7}
