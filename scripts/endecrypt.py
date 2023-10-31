from cryptography.fernet import Fernet
import os

path = __file__.replace("\scripts\endecrypt.py","")


def encrypt():
    if os.path.exists(path + "\\files\\ekey.key"):
        keyfp = open(f"{path}\\files\\ekey.key", "rb")
        key = keyfp.read()

    else:
        key = Fernet.generate_key()
        with open(f"{path}\\files\\ekey.key", "wb") as keyfp:
            keyfp.write(key)
            keyfp.close()

    fernet = Fernet(key)
    with open(f"{path}\\files\\passwords.csv", "rb") as passwordfp:
        passwords = passwordfp.read()
        passwordfp.close()

    encrypted = fernet.encrypt(passwords)

    with open(f"{path}\\files\\passwords.csv", "wb") as passwordfp:
        passwordfp.write(encrypted)
        passwordfp.close()

def decrypt():
    if os.path.exists(path + "\\files\\ekey.key"):
        keyfp = open(f"{path}\\files\\ekey.key", "rb")
        key = keyfp.read()

    else:
        key = Fernet.generate_key()
        with open(f"{path}\\files\\ekey.key", "wb") as keyfp:
            keyfp.write(key)
            keyfp.close()

    fernet = Fernet(key)
    with open(f"{path}\\files\\passwords.csv", "rb") as passwordfp:
        passwords = passwordfp.read()
        passwordfp.close()

    decrypted = fernet.decrypt(passwords)

    while (decrypted.decode("utf-8")[0] != "~"):
        decrypted = fernet.decrypt(decrypted)
        

    return decrypted.decode("utf-8")

if __name__ == "__main__":
    for i in range(5):
        encrypt()

    print(decrypt())