from cryptography.fernet import Fernet


#Encriptar los valores en bytes para guardar los resultados en valores de ascii
def encrypter(password:str):
    f = Fernet(b'FINEHtwMUOxgvyYM9fOvpXcQHYDDZKb3-NKPWTrZN5g=')
    b_password = bytes(password,'ascii')
    encrypter_password = f.encrypt(b_password)
    return encrypter_password.decode('ascii')

#Desenncriptar los valores en bytes para guardar los resultados en valores de ascii
def descrypt(password:str):
    f = Fernet(b'FINEHtwMUOxgvyYM9fOvpXcQHYDDZKb3-NKPWTrZN5g=')
    b_password = bytes(password,'ascii')
    encrypter_descrypt = f.descrypt(b_password)
    return encrypter_descrypt.decode('ascii')