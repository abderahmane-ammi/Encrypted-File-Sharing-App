from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(filename + ".enc", 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(filename.replace(".enc", "_decrypted"), 'wb') as dec_file:
        dec_file.write(decrypted)

# Example usage:
# key = generate_key()
# encrypt_file("secret.txt", key)
# decrypt_file("secret.txt.enc", key)
