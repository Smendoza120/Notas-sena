#Diseñe un algoritmo para seleccionar un menú con 10 operaciones matemáticas básicas: suma, resta, multiplicación, división, módulo, cuadrado, raíz cuadrada, potencia, porcentaje y un número aleatorio. 

import math
import random

opcion = 0
primerNumero = 0
segundoNumero = 0
finalizar = 'No'

while True:
  menu = int(input(f"-------- Operaciones Matematicas --------\n"
      f"Selecciona la opreacion que deseas hacer:\n"
      f"1) Suma\n"
      f"2) Resta\n"
      f"3) Multiplicación\n"
      f"4) División\n"
      f"5) Módulo\n"
      f"6) Cuadrado\n"
      f"7) Raiz cuadrada\n"
      f"8) Potencia\n"
      f"9) Porcentaje\n"
      f"10) Numero al azar\n"
      f"Selecciona: "))
    
  if menu == 1:
    primerNumero = float(input('Digita un numero: '))
    segundoNumero = float(input('digita otro numero: ')) 

    print(f'La suma entre {primerNumero} y {segundoNumero} es = {primerNumero + segundoNumero}')
    finalizar = input('¿Deseas hacer otra operacion? Si / No: ')
    if finalizar == 'No' or finalizar == 'no':
      break

  elif menu == 2:
    primerNumero = float(input('Digita un numero: '))
    segundoNumero = float(input('digita otro numero: '))

    print(f'La resta entre {primerNumero} y {segundoNumero} es = {primerNumero - segundoNumero}')
    finalizar = input('¿Deseas hacer otra operacion? Si / No: ')
    if finalizar == 'No' or finalizar == 'no':
      break
    
  elif menu == 3:
    primerNumero = float(input('Digita un numero: '))
    segundoNumero = float(input('digita otro numero: '))

    print(f'La multiplicacion entre {primerNumero} y {segundoNumero} es = {primerNumero * segundoNumero}')
    finalizar = input('¿Deseas hacer otra operacion? Si / No: ')
    if finalizar == 'No' or finalizar == 'no':
      break

  elif menu == 4:
    primerNumero = float(input('Digita un numero: '))
    segundoNumero = float(input('digita otro numero: '))

    if segundoNumero != 0:
      print(f'La division entre {primerNumero} y {segundoNumero} es = {primerNumero / segundoNumero}')
    else :
      print(f'No es posible la divicion entre 0')

    finalizar = input('¿Deseas hacer otra operacion? Si / No: ')
    if finalizar == 'No' or finalizar == 'no':
      break

  elif menu == 5:
    primerNumero = float(input('Digita un numero: '))
    segundoNumero = float(input('digita otro numero: '))

    print(f'El modulo entre {primerNumero} y {segundoNumero} es = {primerNumero % segundoNumero}')
    finalizar = input('¿Deseas hacer otra operacion? Si / No: ')
    if finalizar == 'No' or finalizar == 'no':
      break

  elif menu == 6:
    primerNumero = float(input('Digita un numero: '))

    print(f'El cuadrado {primerNumero} es = {primerNumero**2}')
    finalizar = input('¿Deseas hacer otra operacion? Si / No: ')
    if finalizar == 'No' or finalizar == 'no':
      break

  elif menu == 7:
    primerNumero = float(input('Digita un numero: '))

    print(f'La raiz cuadrada de {primerNumero} es = {round(math.sqrt(primerNumero), 1)}')
    finalizar = input('¿Deseas hacer otra operacion? Si / No: ')
    if finalizar == 'No' or finalizar == 'no':
      break

  elif menu == 8:
    primerNumero = float(input('Digita la base: '))
    segundoNumero = float(input('digita el exponente: '))

    print(f'La potencia de {primerNumero} a la {segundoNumero} es = {primerNumero ** segundoNumero}')
    finalizar = input('¿Deseas hacer otra operacion? Si / No: ')
    if finalizar == 'No' or finalizar == 'no':
      break

  elif menu == 9:
    primerNumero = float(input('Digita el porcentaje: '))
    segundoNumero = float(input('Digita la cantidad: '))

    print(f'El {primerNumero} % de {segundoNumero} es = {(primerNumero * segundoNumero)/100}')
    finalizar = input('¿Deseas hacer otra operacion? Si / No: ')
    if finalizar == 'No' or finalizar == 'no':
      break

  elif menu == 10:
    print(f'Tu numero al azar es = {random.randint(1, 100)}')
    finalizar = input('¿Deseas hacer otra operacion? Si / No: ')
    if finalizar == 'No' or finalizar == 'no':
      break