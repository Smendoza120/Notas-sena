#Diseñe un algoritmo que muestre un menú para la selección (1. Triángulo, 2. Rectángulo y 3. Círculo); luego pida los datos necesarios para la solución y muestre en pantalla el nombre de la figura, su área en unidades cuadradas y su perímetro en unidades simples. Recuerde que no existen áreas o perímetros menores o iguales a cero.

import math

menu = 0

primerLado = 0
segundoLado = 0
tercerLado = 0

repetir = True

while (repetir != False) :
  menu = int(input(f'-----------MENU-----------\n'
    f'Selecciona la figura deseada\n'
    f'1) Triangulo\n'
    f'2) Rectangulo\n'
    f'3) Circulo\n'
    f'Seleccion: '))

  if menu == 1:
    primerLado = float(input('Digita el primer lado'))
    segundoLado = float(input('Digita el segundo lado'))
    tercerLado = float(input('Digita el tercer lado'))

    perimetro = primerLado + segundoLado + tercerLado

    semiPerimetro = perimetro / 2
    
    if primerLado > 0 and segundoLado > 0 and tercerLado > 0:
      area = round(math.sqrt(semiPerimetro * (semiPerimetro - primerLado) * (semiPerimetro - segundoLado) * (semiPerimetro - tercerLado)), 1)

      print(f'Tu figura es un triangulo\n'
            f'El perimetro del triangulo es: {perimetro}\n'
            f'El area del triangulo es: {area} cm²'
            )

    elif primerLado == 0 or segundoLado == 0 or tercerLado == 0 :
      print('Ningun lado puede ser 0 o negativo')

    repetir = int(input(f'¿Deseas realizar otra operación?\n'
                        f'1)Si 2)No'))
    
    if repetir != 2: 
      repetir = True
    else :
      repetir = False

  elif menu == 2: 
    primerLado = float(input('Digita el primer lado'))
    segundoLado = float(input('Digita el segundo lado'))

    if primerLado > 0 and segundoLado > 0:
      perimetro = (primerLado * 2) + (segundoLado * 2)
      area = primerLado * segundoLado

      print(f'Tu figura es un rectangulo\n'
            f'El perimetro del rectangulo es: {perimetro}\n'
            f'El area del rectangulo es: {area} cm²'
            )

    elif primerLado == 0 or segundoLado == 0:
      print('Ningun lado puede ser 0 o negativo')

    repetir = int(input(f'¿Deseas realizar otra operación?\n'
                        f'1)Si 2)No'))
    if repetir != 2: 
      repetir = True
    else :
      repetir = False

  elif menu == 3:
    primerLado = float(input('Digita el radio'))

    if primerLado > 0:
      perimetro = round((2 * math.pi * primerLado), 1)
      area = round((math.pi * primerLado ** 2), 1)

      print(f'Tu figura es un circulo\n'
            f'El perimetro del circulo es: {perimetro}\n'
            f'El area del circulo es: {area} cm²'
            )
    elif primerLado == 0 or segundoLado == 0:
      print('Ningun lado puede ser 0 o negativo')

    repetir = int(input(f'¿Deseas realizar otra operación?\n'
                        f'1)Si 2)No'))
    if repetir != 2: 
      repetir = True
    else :
      repetir = False

  else :
    print('') 
    repetir = int(input(f'¡Datos erroneos!\n'
                        f'¿Deseas realizar otra operación?\n'
                        f'1)Si 2)No'))
    if repetir != 2: 
      repetir = True
    else :
      repetir = False


