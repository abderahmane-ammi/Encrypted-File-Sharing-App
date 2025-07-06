# Encrypted File Sharing App

Encrypt and decrypt files using AES-based symmetric encryption (Fernet).

## Features
- File encryption with unique key
- Secure file sharing
- Easy to use and extend

## Usage
1. Generate a key using `generate_key()`
2. Encrypt file: `encrypt_file("yourfile.txt", key)`
3. Decrypt file: `decrypt_file("yourfile.txt.enc", key)`
4. Share key securely with recipient
