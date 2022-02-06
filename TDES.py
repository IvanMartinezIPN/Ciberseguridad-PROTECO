from Crypto.Cipher import DES3
from hashlib import md5

while True:
    print('Selecciona una de las siguients opciones:\n\t1- Cifrar\n\t2- Descifrar\n\t3- Salir')
    opc = input('Opcion: ')
    if opc not in ['1', '2']:
        break
    ruta_archivo = input('Ingresa la ruta de tu archivo: ')
    llave = input('Ingresa tu llave: ')

    llave_hash = md5(llave.encode('ascii')).digest()

    tdes_llave = DES3.adjust_key_parity(llave_hash)
    cifrar = DES3.new(tdes_llave, DES3.MODE_EAX, nonce=b'0')

    with open(ruta_archivo, 'rb') as input_file:
        file_bytes = input_file.read()

        if opc == '1':
            archivo = cifrar.encrypt(file_bytes)
        else:
            archivo = cifrar.decrypt(file_bytes)

    with open(ruta_archivo, 'wb') as output_file:
        output_file.write(archivo)
