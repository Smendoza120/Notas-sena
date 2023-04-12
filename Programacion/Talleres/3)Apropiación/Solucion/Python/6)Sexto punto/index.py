# Diseñe un algoritmo que solicite dos números y los divida, como resultado debe mostrar en pantalla (La división del número A entre el número B es: resultado). Si el denominador es cero, deben salir en pantalla: Imposible la división por 0.

dividendo = float(input('Ingresa el dividendo: '))
divisor = float(input('Ingresa el divisor: '))

if divisor != 0:
    print(
        f"La division de {dividendo} entre {divisor} es: {dividendo / divisor}")
else:
    print("imposible la division por 0")
