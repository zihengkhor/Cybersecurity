Someone encrypted a message using AES in ECB mode but they weren’t very careful with their key.  
Turns out it’s derived from something as simple as the current time!  
Can you uncover the key and decrypt the flag?  

[encryption.py](https://github.com/user-attachments/files/30419131/encryption.py)  
from hashlib import sha256  
import time  
from Crypto.Cipher import AES  
from Crypto.Util.Padding import pad  

def encrypt(plaintext: str, timestamp: int) -> str:  
      &ensp;timestamp = int(time.time())  
      &ensp;key = sha256(str(timestamp).encode()).digest()[:16]  
      &ensp;cipher = AES.new(key, AES.MODE_ECB)  
      &ensp;padded = pad(plaintext.encode(), AES.block_size)  
      &ensp;ciphertext = cipher.encrypt(padded)  
      &ensp;return ciphertext.hex()  

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

Flag: picoCTF{sa3S_sEc9t_fbbd0fb7}
