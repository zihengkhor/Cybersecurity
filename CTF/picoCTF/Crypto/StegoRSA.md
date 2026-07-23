**StegoRSA**

-	image.jpg metadata
-	convert hex to private key
-	save private key to .pem file
-	pem (Privacy-Enhanced Mail) format to store certificates, private and public keys
-	openssl pkeyutl -decrypt -inkey your_key.pem -in file.enc -out decrypted_file.txt
-	flag: picoCTF{rs4_k3y_1n_1mg_ce170c3d}
