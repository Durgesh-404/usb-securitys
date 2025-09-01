from cryptography.fernet import Fernet

KEY = Fernet.generate_key()
cipher = Fernet(KEY)

def encrypt_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    encrypted = cipher.encrypt(data)
    with open(file_path, 'wb') as f:
        f.write(encrypted)

def decrypt_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    decrypted = cipher.decrypt(data)
    with open(file_path, 'wb') as f:
        f.write(decrypted)
