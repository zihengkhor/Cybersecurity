picoCTF2025

**EVEN RSA CAN BE BROKEN???** 

-  factordb to find 2 prime numbers
-  p, q
-  d = inverse(e, (p-1)*(q-1))
-  decrypted_message = pow(encrypted_message, d, p*q)
-  print(long_to_bytes(decrypted_message).decode())
-  flag: picoCTF{tw0_1$_pr!m3de643ad5}
