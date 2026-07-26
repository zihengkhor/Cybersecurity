**The Cursed Barrier Terminal**  
Author: @KnuckleHead (IU)

Satoru Gojo locked the higher-ups out of the Cursed Tool vault using a custom barrier interface.  
To retrieve the Special Grade Cursed Tool, sorcerers must authenticate with Special Grade privileges.

The website given:
<img width="1855" height="881" alt="image" src="https://github.com/user-attachments/assets/3a95b05a-284a-40b5-91a4-bd1eb763a1a1" />

-  Inspect Element -> Application -> Cookies
-  Here we found the session cookies of the website

<img width="1020" height="467" alt="image" src="https://github.com/user-attachments/assets/5443b613-8723-4be0-9622-533ce9b6df2b" />

-  Session cookie: "eyJ1c2VybmFtZSI6ICJzb3JjZXJlcl9hcHByZW50aWNlIiwgInJhbmsiOiAiZ3JhZGVfNCIsICJpc19hZG1pbiI6IGZhbHNlfQ=="
-  It is encrypted using base64 format
-  Decrypted format: {"username": "sorcerer_apprentice", "rank": "grade_4", "is_admin": false}

Hint: PERMISSIONS DENIED: GRADE 4 sorcerers cannot inspect Special Grade artifacts.
-  We change the dictionary pair "is_admin": false into "is_admin": true
-  Encrypt it using base64 format: "eyJ1c2VybmFtZSI6ICJzb3JjZXJlcl9hcHByZW50aWNlIiwgInJhbmsiOiAiZ3JhZGVfNCIsICJpc19hZG1pbiI6IHRydWV9"
-  Paste it back to the session cookies

<img width="1847" height="867" alt="image" src="https://github.com/user-attachments/assets/202a5baa-9e22-4719-b9f5-4028e688324c" />

We found our flag after refreshing the website
-  Flag: TriHack26{b4rr13r_cl4ss_s3ss10n_t4mp3r_s4t0ru}
