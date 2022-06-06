def run():

    # Escribir un programa que pregunte al usuario su edad y
    # muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)


    edad = int(input("¿Cuál es tu edad? "))
    for i in range(1, edad+1):
        pass


    # Escribir un programa que pida al usuario un número entero positivo y
    # muestre por pantalla todos los números impares desde 1 hasta ese número
    # separados por comas

    numero = int(input('Ingresa un numero entero positivo '))
    lista = [i for i in range(1, numero+1) if i % 2 != 0]
    pass


    # Escribir un programa que pida al usuario un número entero y muestre por
    # pantalla un triángulo rectángulo como el de más abajo, de altura el
    # número introducido.

    numero = int(input('Ingresa un numero entero positivo '))
    lista = [i for i in range(1, numero + 1)]
    for i in lista:
        # print(i * "*")
        pass


    # Escribir un programa que muestre por pantalla la tabla de multiplicar
    # del 1 al 10.

    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end="\t")
        print("")
        pass

    # Escribir un programa que almacene la cadena de caracteres contraseña
    # en una variable, pregunte al usuario por la contraseña hasta que
    # introduzca la contraseña correcta

    password = input("Ingrese una contraseña: ")
    intento = input('Ingresa la contraseña de nuevo: ')
    while intento != password:
        intento = input('Esa no era la contraseña, hazlo de nuevo: ')








if __name__ == '__main__':
    run()
