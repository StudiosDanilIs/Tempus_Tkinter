import mysql.connector

# Configura los detalles de tu base de datos
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "210605",
    "database": "registro"
}

try:
    # Intenta establecer la conexión
    connection = mysql.connector.connect(**db_config)
    if connection.is_connected():
        print("¡Conexión exitosa!")

        # Ejemplo de consulta: selecciona todos los registros de una tabla
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM usuarios")
        rows = cursor.fetchall()

        # Imprime los resultados
        for row in rows:
            print(row)

        # Cierra la conexión
        cursor.close()
        connection.close()
    else:
        print("No se pudo conectar a la base de datos.")
except Exception as e:
    print(f"Error: {e}")
