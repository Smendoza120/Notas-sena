/*
 *Diseñe un programa (en consola) que solicite 3 números por teclado y saque los números
 *ordenados ascendente o descendente según lo decida el usuario.
 */

let repetir = 1;

do {
  let orden = Number(
    prompt(`
      ¿Como quieres ordenar tus numeros?
      1) Acendente
      2) Decendente
    `)
  );

  let numero1 = Number(prompt("Digita el primer numero"));
  let numero2 = Number(prompt("Digita el segundo numero"));
  let numero3 = Number(prompt("Digita el tercer numero"));

  let arreglo = [numero1, numero2, numero3];
  
  let aux = 0;

  switch (orden) {
    case 1:
      for (let i = 1; i < arreglo.length; i++) {
        for (let j = 0; j < arreglo.length - i; j++) {
          if (arreglo[j] > arreglo[j + 1]) {
            aux = arreglo[j];
            arreglo[j] = arreglo[j + 1];
            arreglo[j + 1] = aux;
          }
        }
      }
      alert(`Los numeros organizados acendentemente son: ${arreglo}`)
      repetir = Number(prompt(`
        ¿Deseas ordenar otros numeros?
        1) Si
        2) No  
      `));
      break;

    case 2:
      for (let i = 1; i < arreglo.length; i++) {
        for (let j = 0; j < arreglo.length - i; j++) {
          if (arreglo[j] < arreglo[j + 1]) {
            aux = arreglo[j];
            arreglo[j] = arreglo[j + 1];
            arreglo[j + 1] = aux;
          }
        }
      }
      alert(`Los numeros organizados decendentemente son: ${arreglo}`)
      repetir = Number(prompt(`
        ¿Deseas ordenar otros numeros?
        1) Si
        2) No  
      `));
      break;

    default:
      break;
  }
} while (repetir === 1);
