from cryptography.fernet import Fernet

key = Fernet.generate_key() # key to encrypt and decrypt
print("Enter the password you would like to use: ")
pword = input() # User entered password
password = pword.encode() # passsword for something

go = Fernet(key) # object to encrypt and decrypt
encrypted = go.encrypt(password)
decrypted = go.decrypt(encrypted)

# Output stats
print("Your key: " + str(key))
print("Password: " + str(password))
print("Encrypted password: " + str(encrypted))
print("decrypted password: " + str(decrypted))

# TODO: Clean up
# TODO: Store encryted password in database
# TODO: Use key to access encrypted passwords in database