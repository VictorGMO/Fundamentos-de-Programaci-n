import random

# Definimos las ciudades y los días de la semana
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4  # Número de semanas a considerar

# Creación de la matriz 3D con temperaturas predefinidas
temperaturas = [
    {"ciudad": "Quito", "semanas": [
        [
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 21},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 16}
        ] for _ in range(semanas)
    ]},
    {"ciudad": "Guayaquil", "semanas": [
        [
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 26}
        ] for _ in range(semanas)
    ]},
    {"ciudad": "Cuenca", "semanas": [
        [
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 12},
            {"day": "Domingo", "temp": 11}
        ] for _ in range(semanas)
    ]}
]

# Función para calcular el promedio de temperaturas por ciudad
def calcular_promedio_ciudad(temperaturas):
    """ Calcula y muestra la temperatura promedio por ciudad y semana. """
    for ciudad in temperaturas:
        print(f"Ciudad: {ciudad['ciudad']}")
        for i, semana in enumerate(ciudad['semanas']):
            promedio = sum(dia['temp'] for dia in semana) / len(semana)
            print(f"  Semana {i + 1}: Promedio de temperatura = {promedio:.2f}°C")
        print()

# Llamada a la función para calcular promedios
calcular_promedio_ciudad(temperaturas)
