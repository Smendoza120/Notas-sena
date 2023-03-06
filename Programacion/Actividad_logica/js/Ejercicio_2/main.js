//*Dise�e un programa (en consola) que encuentre x n�meros de la sucesi�n de Fibonacci, x lo
//*define el usuario por teclado.
//*fibonatcci es la suma del numero anterior por el mismo numero 1+1= 2 +1 = 3 + 2 = 5

function fibonacci(n) {
  let a = 0;
  let b = 1;
  let c = n; //Variable

  for (let i = 0; i <= n; i++) {
    c = a + b;
    a = b;
    b = c;
    console.log(c);
  }

  return c;
}

fibonacci(5);
