// Dise�e un programa (en consola) que permita hacer las operaciones suma, resta
// multiplicaci�n, divisi�n, potencia y porcentaje, con un men� utilizando el switch.

Algoritmo operacion
	Repetir
		Escribir "�Que operacion deseas realizar?"
		Escribir "1) Suma"
		Escribir "2) Resta"
		Escribir "3) Multiplicaci�n"
		Escribir "4) Divisi�n"
		Escribir "5) Residuo"
		Escribir "6) Potencia"
		Leer opera
		
		Segun opera Hacer
			1:
				Escribir "Escribe el primer numero"
				Leer num1
				Escribir "Escribe el segundo numero"
				leer num2
				Escribir "El resultado de la suma es: ", (num1 + num2)
				Escribir "�Deseas hacer otra operaci�n?"
				Leer  continua
			2:
				Escribir "Escribe el primer numero"
				Leer num1
				Escribir "Escribe el segundo numero"
				leer num2
				Escribir "El resultado de la resta es: ", (num1 - num2)
				Escribir "�Deseas hacer otra operaci�n?"
				Leer  continua
			3:
				Escribir "Escribe el primer numero"
				Leer num1
				Escribir "Escribe el segundo numero"
				leer num2
				Escribir "El resultado de la multiplicaci�n es: ", (num1 * num2)
				Escribir "�Deseas hacer otra operaci�n?"
				Leer  continua
			4:
				Escribir "Escribe el primer numero"
				Leer num1
				Escribir "Escribe el segundo numero"
				leer num2
				Escribir "El resultado de la divisi�n es: ", (num1 / num2)
				Escribir "�Deseas hacer otra operaci�n?"
				Leer  continua
			5:
				Escribir "Escribe el primer numero"
				Leer num1
				Escribir "Escribe el segundo numero"
				leer num2
				Escribir "El residuo de la divisi�n es: ", (num1 % num2)
				Escribir "�Deseas hacer otra operaci�n?"
				Leer  continua
			6:
				Escribir "Escribe el primer numero"
				Leer num1
				Escribir "Escribe el segundo numero"
				leer num2
				Escribir "El la potencia de ", num1, " a la ", num2, " es: ", (num1 ^ num2);
				Escribir "�Deseas hacer otra operaci�n?"
				Leer  continua
			De Otro Modo:
				Escribir "Opcion incorrecta, digita una opcion de 1 a 5"
				Leer  continua
		Fin Segun
	Hasta Que continua == 0;
FinAlgoritmo
