from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)
plaintext = "secret".encode()
token = fernet.encrypt(plaintext)
print(token)
decrypted_text = fernet.decrypt(token)
print(decrypted_text)