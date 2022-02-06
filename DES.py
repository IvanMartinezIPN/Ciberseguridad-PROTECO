from Crypto.Cipher import DES
from secrets import token_bytes

llave = token_bytes(8)

def cifrar(mensaje):
    cifrar = DES.new(llave, DES.MODE_EAX)
    nonce = cifrar.nonce
    texto_cifrado, tag = cifrar.encrypt_and_digest(mensaje.encode('ascii')) 
    return nonce,texto_cifrado,tag

def decrypt(nonce,cifrar,tag):
    cifrar = DES.new(llave,DES.MODE_EAX, nonce = nonce)
    texto_plano = cifrar.decrypt(texto_cifrado)
    try:
        cifrar.verify(tag)
        return texto_plano.decode('ascii')
    except:
        return False
nonce, texto_cifrado, tag = cifrar(input('Ingresa tu mensaje : '))
texto_plano = decrypt(nonce, texto_cifrado, tag)

print(f'Texto cifrado: {texto_cifrado}')

if not texto_plano:
    print('Mensaje vulnerado')
else:
    print(f'El mensaje es: {texto_plano}' )