import hashlib

# Get the user's password as input
user_password = input("Enter your password: ")

# Create a new SHA-256 hash object
sha256_hash = hashlib.sha256()

# Encode the user's password as bytes
password_bytes = user_password.encode('utf-8')

# Update the hash object with the password bytes
sha256_hash.update(password_bytes)

# Calculate the SHA-256 hash
hashed_password = sha256_hash.hexdigest()

# Display the original password and its hash
print(f'Original Password: {user_password}')
print(f'SHA-256 Hash: {hashed_password}')
