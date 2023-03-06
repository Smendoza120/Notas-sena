//Diseñe un programa (en consola) que solicite 3 números por teclado y saque los números 
//ordenados ascendente o descendente según lo decida el usuario. 

Algoritmo ordenamiento
	continuar<-1
	
	Repetir
		Escribir "Digita el primer numero";
		Leer num1
		Escribir "Digita el segundo numero";
		Leer num2
		Escribir "Digita el tercer numero";
		Leer num3
		Dimension datos[num1,num2,num3];
		//datos[0] = num1;
		//datos[1] = num2;
		//datos[2] = num3;
		aux<-0
		
		Para i <- 1 Hasta 3 Con Paso 1 Hacer
			Para j <- 0 Hasta 3-i Con Paso 1 Hacer
				si datos[j] > datos[j+1] Entonces
					aux <- datos[j];
					datos[j]<-datos[j+1]
					datos[j+1]<-aux
				FinSi
			FinPara
		Fin Para
		
		para i<-0 Hasta 2 Con Paso 1 Hacer
			Escribir Sin Saltar datos[i], " ";
		FinPara
		
	Hasta Que continuar == 1
	
FinAlgoritmo
