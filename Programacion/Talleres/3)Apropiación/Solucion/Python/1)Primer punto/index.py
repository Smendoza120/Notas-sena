#Diseñe un algoritmo que muestre en pantalla su nombre, sexo, edad, salario (incluyendo centavos) y si tiene o no vehículo de transporte.

nombre = 'Harold Yulian Sanchez Alcantar'
sexo = 'Masculino'
edad = 24
salario = 1_020_000
vehiculo = False
tengoVehiculo = ("No tengo vehiculo", "Tengo vehiculo")[vehiculo]

print(f"Nombre: {nombre}\n"\
      f"Sexo: {sexo}\n" \
      f"Edad: {edad}\n" \
      f"Salario: {salario}\n"\
      f"Vehiculo: {tengoVehiculo}")

