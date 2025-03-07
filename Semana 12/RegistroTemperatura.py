# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    {"ciudad": "Quito", "semanas": [
        [   # Semana 1
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 21},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 16}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 17}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 18},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 15}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 18}
        ]
    ]},
    {"ciudad": "Guayaquil", "semanas": [
        [   # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 26}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 27}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 25}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 34},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 28}
        ]
    ]},
    {"ciudad": "Cuenca", "semanas": [
        [   # Semana 1
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 12},
            {"day": "Domingo", "temp": 11}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 13},
            {"day": "Domingo", "temp": 12}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 13},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 11},
            {"day": "Domingo", "temp": 10}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 13}
        ]
    ]}
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad in temperaturas:
    print(f"Ciudad: {ciudad['ciudad']}")
    for i, semana in enumerate(ciudad['semanas']):
        suma = sum(dia['temp'] for dia in semana)
        promedio = suma / len(semana)
        print(f"  Semana {i+1}: Promedio de temperatura = {promedio:.2f}°C")
    print()
