The website given:
<img width="1855" height="878" alt="image" src="https://github.com/user-attachments/assets/d7e4ec69-d4c5-4867-bb51-4fe5fbb8b9a7" />

-  Inspect Element -> Application -> Cookies
-  Here we found the session cookies of the website

<img width="1022" height="352" alt="image" src="https://github.com/user-attachments/assets/8e981e05-c5e0-4267-a323-622c1b22bd47" />

-  "cm9sZT1zdHVkZW50" is encrypted using base64 format
-  decrypted format: role=student

-  hint: Only the Headmaster is authorized to view the Restricted Section.
-  we rename the string into "role=headmaster"
-  encrypt it using base64 format: "cm9sZT1oZWFkbWFzdGVy", paste it back to the session cookies

<img width="1853" height="876" alt="image" src="https://github.com/user-attachments/assets/89f90959-9b3a-4161-bdaa-1ed8dcb2d321" />
-  we found our flag after refreshing the website

-  Flag: TriHack26{4l0h0m0r4_byp455_5ucc355}
