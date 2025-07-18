from cryptography.fernet import Fernet

# Generate a valid key
key = Fernet.generate_key()

# Save it securely in a file
with open("key.key", "wb") as key_file:
    key_file.write(key)

print("✅ New encryption key generated and saved in key.key")