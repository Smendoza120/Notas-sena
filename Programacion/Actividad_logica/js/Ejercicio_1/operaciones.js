/*
 *Diseñe un programa (en consola) que permita hacer las operaciones suma, resta
 *multiplicación, división, potencia y porcentaje, con un menú utilizando el switch.
 */

let numero1;
let numero2;
let continuar = 1;

do {
  let mensaje = Number(
    prompt(`
    Bienvenido a la calculadora: 
    selecciona la siguiente opcion para hacer la operación deseada:
    1) Suma
    2) Resta
    3) Multiplicacion
    4) Division
    5) Residuo
    6) Potencia
  `)
  );
  switch (mensaje) {
    case 1:
      numero1 = Number(prompt("Digita el primer numero"));
      numero2 = Number(prompt("Digita el segundo numero"));
      alert(`La suma de ${numero1} y ${numero2} es de: ${numero1 + numero2}`);
      continuar = Number(
        prompt(`
        ¿Deseas hacer otra operación?
        1) Si
        2) No
      `)
      );
      break;
    case 2:
      numero1 = Number(prompt("Digita el primer numero"));
      numero2 = Number(prompt("Digita el segundo numero"));
      alert(`La resta de ${numero1} y ${numero2} es de: ${numero1 - numero2}`);
      continuar = Number(
        prompt(`
        ¿Deseas hacer otra operación?
        1) Si
        2) No
      `)
      );
      break;
    case 3:
      numero1 = Number(prompt("Digita el primer numero"));
      numero2 = Number(prompt("Digita el segundo numero"));
      alert(
        `La multiplicación de ${numero1} y ${numero2} es de: ${
          numero1 * numero2
        }`
      );
      continuar = Number(
        prompt(`
        ¿Deseas hacer otra operación?
        1) Si
        2) No
      `)
      );
      break;
    case 4:
      numero1 = Number(prompt("Digita el primer numero"));
      numero2 = Number(prompt("Digita el segundo numero"));
      alert(
        `La division de ${numero1} y ${numero2} es de: ${numero1 / numero2}`
      );
      continuar = Number(
        prompt(`
        ¿Deseas hacer otra operación?
        1) Si
        2) No
      `)
      );
      break;
    case 5:
      numero1 = Number(prompt("Digita el primer numero"));
      numero2 = Number(prompt("Digita el segundo numero"));
      alert(
        `El residuo de ${numero1} y ${numero2} es de: ${numero1 % numero2}`
      );
      continuar = Number(
        prompt(`
        ¿Deseas hacer otra operación?
        1) Si
        2) No
      `)
      );
      break;
    case 6:
      numero1 = Number(prompt("Digita el numero"));
      numero2 = Number(prompt("Digita la potencia"));
      alert(
        `La potencia de ${numero1} a la ${numero2} es de: ${numero1 ** numero2}`
      );
      continuar = Number(
        prompt(`
        ¿Deseas hacer otra operación?
        1) Si
        2) No
      `)
      );
      break;
    default:
      alert(
        "Numero erroneo, porfavor digita un numero del 1 al 5, intentalo nuevamente"
      );
      continuar = Number(
        prompt(`
        ¿Deseas intentarlo nuevamente?
        1) Si
        2) No
      `)
      );
      break;
  }
} while (continuar === 1);
