import rsa

def generar_llave():
    (llave_publica,llave_privada) = rsa.newkeys(1024)
    with open('llavesrsa/llave_publica.pem','wb') as archivo:
        archivo.write(llave_publica.save_pkcs1('PEM'))
    with open('llavesrsa/llave_privada.pem','wb') as archivo:
        archivo.write(llave_privada.save_pkcs1('PEM'))

def cargar_llave():
    with open('llavesrsa/llave_publica.pem','rb') as archivo:
        llave_publica = rsa.PublicKey.load_pkcs1(archivo.read())
    
    with open('llavesrsa/llave_privada.pem','rb') as archivo:
        llave_privada = rsa.PrivateKey.load_pkcs1(archivo.read())
    return llave_publica,llave_privada

def cifrar(mensaje,llave):
    return rsa.encrypt(mensaje.encode('ascii'),llave)

def descifrar(texto, llave):
    try:
        return rsa.decrypt(texto,llave).decode('ascii')
    except:
        return False

def firma(mensaje,llave):
    return rsa.sign(mensaje.encode('ascii'),llave, 'SHA-256')

def verificar_firma(mensaje,firma,llave):
    try:
        return rsa.verify(mensaje.encode('ascii'),firma,llave) == 'SHA-256'
    except:
        return False

generar_llave()
llave_publica,llave_privada = cargar_llave()
mensaje = input('Ingresa tu texto a cifrar: ')
texto_cifrado = cifrar(mensaje,llave_publica)
crea_firma = firma(mensaje,llave_privada)
texto_descifrado = descifrar(texto_cifrado,llave_privada)
print(f'Tu mensaje cifrado es: {texto_cifrado}')
print(f'Tu firma es: {crea_firma}')

if texto_descifrado:
    print(f'Texto descifrado: {texto_descifrado}')
else:
    print('Texto no descifrado')

if verificar_firma(texto_descifrado,crea_firma,llave_publica):
    print('Firma verificada')
else:
    print('Firma invalida')