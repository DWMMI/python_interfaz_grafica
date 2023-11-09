cantidad_ninos = int(input("Ingrese la cantidad de niños: "))
cantidad_ninas = int(input("Ingrese la cantidad de niñas: "))

total_estudiantes = cantidad_ninos + cantidad_ninas

porcentaje_ninos = (cantidad_ninos / total_estudiantes) * 100
porcentaje_ninas = (cantidad_ninas / total_estudiantes) * 100

print(f"Porcentaje de niños: {porcentaje_ninos}%")
print(f"Porcentaje de niñas: {porcentaje_ninas}%")
