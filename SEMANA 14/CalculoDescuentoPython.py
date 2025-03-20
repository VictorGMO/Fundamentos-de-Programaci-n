# Creación de la función
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado a una compra.

    Parámetros:
    - monto_total: El monto total de la compra.
    - porcentaje_descuento: El porcentaje de descuento (valor predeterminado 10%).

    Retorna:
    - El monto del descuento calculado.
    """
    # Calcular el descuento
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento


# Llamada a la función
# Ejemplo 1: Usando el valor predeterminado del porcentaje de descuento (10%)
monto_compra_1 = 300
descuento_1 = calcular_descuento(monto_compra_1)
monto_final_1 = monto_compra_1 - descuento_1

# Ejemplo 2: Proporcionando un porcentaje de descuento personalizado
monto_compra_2 = 3000
porcentaje_descuento_2 = 20
descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)
monto_final_2 = monto_compra_2 - descuento_2

# Salida de resultados
print("Resultado de la primera llamada:")
print(f"Monto total de la compra: ${monto_compra_1}")
print(f"Descuento aplicado: ${descuento_1}")
print(f"Monto final a pagar: ${monto_final_1}\n")

print("Resultado de la segunda llamada:")
print(f"Monto total de la compra: ${monto_compra_2}")
print(f"Descuento aplicado: ${descuento_2}")
print(f"Monto final a pagar: ${monto_final_2}")