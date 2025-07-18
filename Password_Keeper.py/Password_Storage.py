from cryptography.fernet import Fernet
import os

# Load the encryption key from file
def load_key():
    return open("key.key", "rb").read()

# Initialize Fernet with the key
key = load_key()
fernet = Fernet(key)

# Encrypt and save password
def save_password():
    account = input("Enter the account/site name: ").strip()
    username = input("Enter the username/email: ").strip()
    password = input("Enter the password: ").strip()

    encrypted_password = fernet.encrypt(password.encode())

    with open("passwords.txt", "a") as f:
        f.write(f"{account} | {username} | {encrypted_password.decode()}\n")

    print("\n✅ Password saved securely!\n")

# View saved passwords
def view_passwords():
    if not os.path.exists("passwords.txt"):
        print("⚠️ No passwords saved yet.")
        return

    with open("passwords.txt", "r") as f:
        for line in f:
            account, username, encrypted_pw = line.strip().split(" | ")
            decrypted_pw = fernet.decrypt(encrypted_pw.encode()).decode()
            print(f"\n🔐 {account} ({username}) → {decrypted_pw}")

# Main program loop
while True:
    print("\n=== Password Manager ===")
    print("1. Save a new password")
    print("2. View saved passwords")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        save_password()
    elif choice == "2":
        view_passwords()
    elif choice == "3":
        print("\n👋 Goodbye! Stay safe.")
        break
    else:
        print("❌ Invalid choice. Try again.")
