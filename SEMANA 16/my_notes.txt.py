# Escritura de Archivo de Texto

# 1. Crear y abrir un archivo llamado 'my_notes.txt' en modo escritura ('w').
with open('my_notes.txt', 'w') as file:
    # 2. Escribir al menos tres líneas de notas personales en el archivo.
    file.write("Nota 1: Hoy es un buen día para aprender Python.\n")
    file.write("Nota 2: Como estan todos.\n")
    file.write("Nota 3: ¡Lindo dia!\n")

# Nota: Usar 'with open()' asegura que el archivo se cierre automáticamente después del bloque.

# Lectura de Archivo de Texto

# 1. Abrir el archivo 'my_notes.txt' en modo lectura ('r').
with open('my_notes.txt', 'r') as file:
    print("Contenido del archivo línea por línea:")
    # 2. Leer el contenido del archivo línea por línea utilizando readline().
    line = file.readline()
    while line:
        # 3. Mostrar en la consola cada línea leída.
        print(line.strip())  # strip() elimina el salto de línea adicional al imprimir.
        line = file.readline()

# Nota:al usar'with open()', no es necesario cerrar el archivo manualmente, ya que se cierra automáticamente al final del bloque(por lo que se).


