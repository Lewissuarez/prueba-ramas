i = 0

while(i != 5):

    print(".:Menu:.")
    print("1. Recibir nombre y año de nacimiento")
    print("2. Calcular edad y mostrar en pantalla")
    print("3. Mostrar saludo de buenas noches al usuario")
    print("4. Contar cuantos años tendra en el 2023")
    print("4. Salir")
    i= int(input("Digite la opcion: "))

    if(i == 1):
        nombre = input(f'Digite el nombre: ')
        anoNacimiento = input(f'Digite el nombre: ')
    elif(i == 2):
        edad = 2022-float(anoNacimiento)
        print(f'La edad de {nombre} es {edad}')
    else:
        print('Digite una opcion valida')