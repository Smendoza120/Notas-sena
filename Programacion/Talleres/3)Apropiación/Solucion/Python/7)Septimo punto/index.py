# Diseñe un algoritmo que muestre un menú: Amarillo = 1, azul = 2, rojo = 3.  Luego solicite al usuario digitar dos de estos números para descifrar la combinación. Ejemplo: 1 y 3, el resultado mostrado en pantalla (su combinación es naranja). Recuerde que el usuario puede colocar el mismo número dos veces y números fuera del rango.

print(f"Agrega 2 numeros para hacer la combinacion de colores\n"
      f"Amarillo = 1 "
      f"Azul = 2 "
      f"Rojo = 3")

primerNumero = int(input('Digita un numero del 1 al 3: '))
segundoNumero = int(input('Digita un numero del 1 al 3: '))
colores = ["Verde", "Naranja", "Violeta", "Amarillo", "Azul", "Rojo"]

if primerNumero == 1 and segundoNumero == 2 or primerNumero == 2 and segundoNumero == 1:
  print(f'La combinacion es {colores[0]}')
elif primerNumero == 1 and segundoNumero == 3 or primerNumero == 3 and segundoNumero == 1:
  print(f'La combinacion es {colores[1]}')
elif primerNumero == 2 and segundoNumero == 3 or primerNumero == 3 and segundoNumero == 2:
  print(f'La combinacion es {colores[2]}')
elif primerNumero == 1 and segundoNumero == 1:
  print(f'La combinacion es {colores[3]}')
elif primerNumero == 2 and segundoNumero == 2:
  print(f'La combinacion es {colores[4]}')
elif primerNumero == 3 and segundoNumero == 3:
  print(f'La combinacion es {colores[5]}')
else :
  print('Datos erroneos')



