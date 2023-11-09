

A = int(input("Introduce el valor de A: "))
B = int(input("Introduce el valor de B: "))

print(f"Valores iniciales: A = {A}, B = {B}")

temp = A
A = B
B = temp

print(f"Valores después del intercambio: A = {A}, B = {B}")
