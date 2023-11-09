A = float(input("Introduce el valor de A: "))
B = float(input("Introduce el valor de B: "))

# Realizar las operaciones
suma = A + B
resta = A - B
multiplicacion = A * B

if B != 0:
    division = A / B
else:
    division = "No se puede dividir por cero"

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
