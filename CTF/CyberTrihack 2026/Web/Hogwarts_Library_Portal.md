Hogwarts Library Portal
Author: @JayZee (IU)

The Restricted Section of the Hogwarts Library holds ancient archival records, but the web portal's security checkpoint blocks standard student credentials.
Access the web portal instance provided by the platform and bypass the portal's access controls to gain entry into the Restricted Section.


The website given:
<img width="1855" height="878" alt="image" src="https://github.com/user-attachments/assets/d7e4ec69-d4c5-4867-bb51-4fe5fbb8b9a7" />

-  Inspect Element -> Application -> Cookies
-  Here we found the session cookies of the website

<img width="1022" height="352" alt="image" src="https://github.com/user-attachments/assets/8e981e05-c5e0-4267-a323-622c1b22bd47" />

-  "cm9sZT1zdHVkZW50" is encrypted using base64 format
-  Decrypted format: role=student

-  Hint: Only the Headmaster is authorized to view the Restricted Section.
-  We rename the string into "role=headmaster"
-  Encrypt it using base64 format: "cm9sZT1oZWFkbWFzdGVy", paste it back to the session cookies

<img width="1853" height="876" alt="image" src="https://github.com/user-attachments/assets/89f90959-9b3a-4161-bdaa-1ed8dcb2d321" />
We found our flag after refreshing the website

-  Flag: TriHack26{4l0h0m0r4_byp455_5ucc355}
