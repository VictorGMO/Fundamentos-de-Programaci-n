#Crear un diccionario llamado informacion_personal
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}
print("=== DICCIONARIOS ===")
print("Diccionario original:", informacion_personal)

#Acceder y modificar el valor asociado con la clave "ciudad"
print("Ciudad original:", informacion_personal["ciudad"])  # Mostrar la ciudad original
informacion_personal["ciudad"] = "Guayaquil"  # Cambiar la ciudad
print("Ciudad modificada:", informacion_personal["ciudad"])  # Mostrar la nueva ciudad

#Verificar si la clave "telefono" existe en el diccionario.
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"  # Agregar un número de teléfono ficticio
print("Teléfono agregado:", informacion_personal["telefono"])

#Eliminar la clave "edad" del diccionario.
del informacion_personal["edad"]
print("Clave 'edad' eliminada.")

#Imprimir el diccionario final
print("\nDiccionario final:")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")