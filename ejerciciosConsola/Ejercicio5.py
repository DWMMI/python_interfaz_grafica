EUROS_A_PESETAS = 166.386

def convertir_euros_a_pesetas(euros):
    pesetas = euros * EUROS_A_PESETAS
    return pesetas

# Ejemplo de uso
monto_euros = float(input("Ingresa la cantidad en euros: "))
resultado_pesetas = convertir_euros_a_pesetas(monto_euros)

print(f"{monto_euros} euros son {resultado_pesetas} pesetas.")
