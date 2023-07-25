import hashlib
import binascii

# Define the PBKDF2 function
def pbkdf2(password, salt, iterations, keylen):
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), iterations, dklen=keylen)
    return binascii.hexlify(dk).decode()

# Ask for user input
# password = input("Please enter the clear text password: ")
# salt = input("Please enter the salt (ASCII string of length 24): ")
password = "hellodai"
salt = "92dcb571d06c2717d7f50849"

# Validate the salt length
if len(salt) != 24:
    print("Invalid salt length. Please enter an ASCII string of length 24.")
else:
    # Generate and print the encrypted password
    encrypted_password = pbkdf2(password, salt, 5000, 32)
    print("Encrypted password:", encrypted_password)