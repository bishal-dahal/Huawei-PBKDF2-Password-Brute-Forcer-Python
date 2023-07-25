# import hashlib
# import binascii

# # Define the PBKDF2 function
# def pbkdf2(password, salt, iterations, keylen):
#     dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), iterations, dklen=keylen)
#     return binascii.hexlify(dk).decode()

# # Set the expected encrypted password
# expected_password = "a97cec2f738f3b851ccaa66cbd64621d70d1e1959b1283248210be80f1fd01af"
# salt = "92dcb571d06c2717d7f50849"

# # Open the wordlist file and the output file
# with open("wordlist.txt", "r") as wordlist_file, open("dec_password.txt", "w") as output_file:
#     for line in wordlist_file:
#         password = line.strip()  # Remove the newline character
#         encrypted_password = pbkdf2(password, salt, 5000, 32)  # Salt is an empty string
#         if encrypted_password == expected_password:
#             print("Match found! The password is:", password)
#             output_file.write(password + '\n')
#             break



import hashlib
import binascii
import time

# Define the PBKDF2 function
def pbkdf2(password, salt, iterations, keylen):
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), iterations, dklen=keylen)
    return binascii.hexlify(dk).decode()

# # Set the expected encrypted password
expected_password = "a97cec2f738f3b851ccaa66cbd64621d70d1e1959b1283248210be80f1fd01af"
salt = "92dcb571d06c2717d7f50849"
# Start the total time counter
start_time_total = time.time()

# Open the wordlist file and the output file
with open("wordlist.txt", "r") as wordlist_file, open("dec_password.txt", "w") as output_file:
    for line in wordlist_file:
        password = line.strip()  # Remove the newline character
        
        # Start the per-line time counter
        start_time_line = time.time()
        
        encrypted_password = pbkdf2(password, salt, 5000, 32)  # Salt is an empty string
        
        # Calculate and print the time taken for this line
        end_time_line = time.time()
        print("Time taken for this line:", end_time_line - start_time_line, "seconds")
        
        if encrypted_password == expected_password:
            print("Match found! The password is:", password)
            output_file.write(password + '\n')
            break

# Calculate and print the total time taken
end_time_total = time.time()
print("Total time taken:", end_time_total - start_time_total, "seconds")