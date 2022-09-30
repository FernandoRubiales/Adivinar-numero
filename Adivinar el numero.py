
# ADIVINA EL NÚMERO - PROYECTO N°3

import random

# Definimos las variables.
posibilidades = 5
limite = 10

# Le damos al usuario el mensaje de bienvenida y comenzamos el juego.
print("Hola, como es tu nombre?")
nombre = input()
print("\nMuy bien " + nombre + " estoy pensando en un número que esta entre el 1 y el "+ str(limite))
print("Intenta adivinarlo, solo tienes " + str(posibilidades) + " posibilidades")

# Definimos la variable para seleccionar un numero aleatoriamente.
adivina = random.randint(1, limite)

# Creamos un ciclo de acuerdo a los intentos posibles que tiene el usuario.
intentos = 0
while intentos < posibilidades:
    numero = int(input("\nIngresa el número que crees correcto:  "))

    if numero == adivina:
        print("\nGANASTE!!")
        break
    elif intentos >= posibilidades -1:
        print("\nPERDISTE")
        break
    else:
        if numero > adivina:
            print("Intenta con un numero mas pequeño")
        else:
            print("Intenta con un numero mas grande")
        
    intentos += 1
