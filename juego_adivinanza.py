import random

numero_secreto = random.randint(1,100)
cant_intentos = 0
cant_max_intentos = 7 
adivinado = False # Variable que colocamos para transformar en TRUE si llegan a adivinar

print("Bienvenido al juego de adivinar el número secreto")

while not adivinado:
    if not cant_intentos < cant_max_intentos:
        print("¡Game Over! No has podido adivinar dentro de los 7 intentos")
        break
    
    entrada = input("Introduce un número del 1 al 100: ") # TODO: convertir a número. #INPUT devuelve un string.
    numero = int(entrada)

    if numero == numero_secreto:
        print("¡Felicidades has adivinado el número secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print("El número es mayor al ingresado")
    else:
        print("El número es menor al ingresado")
    
    cant_intentos += 1
