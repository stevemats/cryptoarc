from cryptography.fernet import Fernet, MultiFernet

key1 = Fernet.generate_key()
key2 = Fernet.generate_key()

fernet1 = Fernet(key1)
fernet2 = Fernet(key2)

plaintext = "Secret".encode()

multi_fernet = MultiFernet([fernet1, fernet2])
token = multi_fernet.encrypt(plaintext)
print(token)

decrypted_text1 = multi_fernet.decrypt(token)
print(decrypted_text1)

key3 = Fernet.generate_key()
fernet3 = Fernet(key3)

multi_fernet2 = MultiFernet([fernet3, fernet1, fernet2])
rotated_token = multi_fernet2.rotate(token)
print(rotated_token)

decrypted_text2 = multi_fernet2.decrypt(rotated_token)
print(decrypted_text2)

multi_fernet3 = MultiFernet([fernet3, fernet2])
decrypted_text3 = multi_fernet3.decrypt(rotated_token)
print(decrypted_text3)
