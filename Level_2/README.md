Server sends md5.
Decrypt, then add 1, then encrypt with SHA-512 and send that back to server.

Run server_to_client_hash.py
Then user passive mode ftp to connect over port 2121.
Download all the files there, and periodically run the python file to renew authentication.

Find id_rsa and convert it to PuTTY using passphrase found: s3cr3t
Now SSH in to the server on port 22.
user: backup
But I am getting a response of: /bin/false not found.
How odd....