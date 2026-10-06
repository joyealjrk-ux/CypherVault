import os
from cryptography.fernet import Fernet
def generate_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)

# Load the key
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

# Encrypt and save password
def save_password(service, username, password):
    key = load_key()                                                    
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())                                                                

    with open("passwords.txt", "a") as file:
        file.write(f"{service},{username},{encrypted_password.decode()}\n")
    print("Password saved successfully!")         
# Retrieve and decrypt password
def retrieve_password(service):
    key = load_key()
    fernet = Fernet(key)

    if not os.path.exists("passwords.txt"):
        print("No passwords stored yet.")
        return

    with open("passwords.txt", "r") as file:
        for line in file:
            stored_service, username, encrypted_password = line.strip().split(",")
            if stored_service == service:
                decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
                print(f"Service: {service}\nUsername: {username}\nPassword: {decrypted_password}")
                return
    print("Service not found.")

# Main menu
def main():
    generate_key()
    print("current working Folder:", os.getcwd())
    while True:
        print("\nPassword Manager")
        print("1. Save a password")
        print("2. Retrieve a password")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            service = input("Enter the service name: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            save_password(service, username, password)
        elif choice == "2":
            service = input("Enter the service name to retrieve: ")
            retrieve_password(service)
        elif choice == "3":
            print("Exiting Password Manager. Stay secure!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print(main()) 
else:                         
    print("invalid")