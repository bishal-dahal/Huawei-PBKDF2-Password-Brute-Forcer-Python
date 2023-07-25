import hashlib
import binascii
import time
from multiprocessing import Pool

# Define the PBKDF2 function
def pbkdf2(password, salt, iterations, keylen):
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), iterations, dklen=keylen)
    return binascii.hexlify(dk).decode()

def check_password(password):
    salt = "92dcb571d06c2717d7f50849"
    return pbkdf2(password, salt, 5000, 32)  # Salt is an empty string

def main():
    # Set the expected encrypted password
    global salt
    expected_password = "a97cec2f738f3b851ccaa66cbd64621d70d1e1959b1283248210be80f1fd01af"

    # Start the total time counter
    start_time_total = time.time()

    # Get the total number of lines
    with open('wordlist.txt') as f:
        total_lines = sum(1 for _ in f)

    passwords = []
    # Open the wordlist file and read all passwords
    with open("wordlist.txt", "r") as wordlist_file:
        passwords = [line.strip() for line in wordlist_file]

    # Create a multiprocessing Pool
    with Pool() as p:
        results = p.map(check_password, passwords)

    # Find the matching password
    for i, encrypted_password in enumerate(results):
        if encrypted_password == expected_password:
            print(f"Match found! The password is: {passwords[i]}")
            with open("dec_password.txt", "w") as output_file:
                output_file.write(passwords[i] + '\n')
            break

    # Calculate and print the total time taken
    end_time_total = time.time()
    print("Total time taken:", end_time_total - start_time_total, "seconds")

if __name__ == '__main__':
    main()