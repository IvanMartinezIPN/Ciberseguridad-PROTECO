
try:
    opcion = input('Selecciona una opcion para ejecutar \n 1.Cifrar archivos \n 2.Cifrar mensajes\n 3. Salir \n Opcion: ')
    if opcion == '2':
        selec = input('Selecciona un metodo de cifrado: \n 1.DES\n 2.AES \n 3. RSA \n Opcion: ')
        if selec == '1':
            import DES
        elif selec == '2':
            import AES
        else:
            import RSA
    elif opcion == '1':
        import TDES
    else:
        exit(0)
except Exception as error:
    print(f'Error {error}')
finally:
    print('Gracias por usar')