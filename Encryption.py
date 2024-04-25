from cryptography.fernet import Fernet


def generateEncryptionkey(filepath):
    try:
        key = getEncryptionKey()
        print("Key already exists")
    except:
        key = Fernet.generate_key()

        with open('Resources/filekey.key', 'wb') as filekey:
            filekey.write(key)


def getEncryptionKey():
    with open('Resources/filekey.key', 'rb') as filekey:
        key = filekey.read()
    return key


def encryptFile(filepath):
    key = getEncryptionKey()
    fernet = Fernet(key)

    with open(filepath, 'rb') as file:
        fileToEncrypt = file.read()

    encrypted = fernet.encrypt(fileToEncrypt)

    with open(filepath, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def decryptFile(filepath):
    key = getEncryptionKey()
    fernet = Fernet(key)

    with open(filepath, 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(filepath, 'wb') as dec_file:
        dec_file.write(decrypted)

def encrypt(data):
    key = getEncryptionKey()
    fernet = Fernet(key)

    encrypted = fernet.encrypt(data)
    return encrypted



def decrypt(data):
    key = getEncryptionKey()
    fernet = Fernet(key)

    decrypted = fernet.decrypt(data)
    return decrypted
