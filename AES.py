from Crypto.Cipher import AES
from secrets import token_bytes

llave = token_bytes(16)

def cifrar(msg):
    cifrar = AES.new(llave, AES.MODE_EAX)
    nonce = cifrar.nonce
    cifrartexto, tag = cifrar.encrypt_and_digest(msg.encode('ascii'))
    return nonce, cifrartexto, tag

def descifrar(nonce, cifrartexto, tag):
    cifrar = AES.new(llave, AES.MODE_EAX, nonce=nonce)
    texto = cifrar.decrypt(cifrartexto)
    try:
        cifrar.verify(tag)
        return texto.decode('ascii')
    except:
        return False

nonce, cifrartexto, tag = cifrar(input('Ingresa tu mensaje: '))
texto = descifrar(nonce, cifrartexto, tag)
print(f'Texto cifrado: {cifrartexto}')
if not texto:
    print('El mensaje ha sido corrompido')
else:
    print(f'Mensaje original: {texto}')