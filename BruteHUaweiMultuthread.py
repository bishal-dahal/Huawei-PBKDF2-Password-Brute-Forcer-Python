import hashlib
import binascii
import time
import concurrent.futures

# Define the PBKDF2 function
def pbkdf2(password, salt, iterations, keylen):
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), iterations, dklen=keylen)
    return binascii.hexlify(dk).decode()

def check_password(password):
    start_time_line = time.time()
    encrypted_password = pbkdf2(password, salt, 5000, 32)  # Salt is an empty string
    end_time_line = time.time()
    result = (password, encrypted_password, end_time_line - start_time_line)
    return result

# # Set the expected encrypted password
expected_password = "a97cec2f738f3b851ccaa66cbd64621d70d1e1959b1283248210be80f1fd01af"
salt = "92dcb571d06c2717d7f50849"

# Start the total time counter:
start_time_total = time.time()

# Get the total number of lines
with open('wordlist.txt') as f:
    total_lines = sum(1 for _ in f)

current_line = 0
# Open the wordlist file and the output file
with open("wordlist.txt", "r") as wordlist_file, open("dec_password.txt", "w") as output_file:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_line = {executor.submit(check_password, line.strip()): line for line in wordlist_file}
        for future in concurrent.futures.as_completed(future_to_line):
            password, encrypted_password, time_taken = future.result()
            current_line += 1
            print(f"Line {current_line}/{total_lines}: Time taken for this line: {time_taken} seconds")
            if encrypted_password == expected_password:
                print("Match found! The password is:", password)
                output_file.write(password + '\n')
                break

# Calculate and print the total time taken
end_time_total = time.time()
print("Total time taken:", end_time_total - start_time_total, "seconds")