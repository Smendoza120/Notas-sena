//Diseñe un programa (en consola) que encuentre x números de la sucesión de Fibonacci, x lo 
//define el usuario por teclado.

Funcion c <- actividad ( n )
	a <- 0
	b <- 1
	c <- n
	
	Para i <- 0 Hasta n Hacer
		Escribir a
		c <- a + b 
		a <- b
		b <- c
	Fin Para
Fin Funcion

Algoritmo Fibonacci
	Escribir "Ingresa el valor de n";
	leer n;
	n <- actividad(n)
FinAlgoritmo
