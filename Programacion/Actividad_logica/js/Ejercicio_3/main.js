/*
*Diseñe un programa (en consola) que encuentre el factorial de un número del 0 al 150 
*después de 150 de colocar un número mayor debe salir factorial es infinito.
*/

function factorial(n){
  let total = 1;

  for(let i = 1; i<= n; i++){
    total *= i;
  }


  if(total > 5.7133839564458505e+262){
    console.log("Es infinito")
  } else {
    console.log(total)
    return total
  }
}

factorial(151)