import mysql.connector

try:
    # Configura los detalles de conexión
    db_config = {
        "host": "127.0.0.1",  # Cambia esto al host correcto
        "user": "root",
        "password": "210605",
        "database": "registro"
    }

    # Crea la conexión
    conn = mysql.connector.connect(**db_config)

    if conn.is_connected():
        print("Conexión exitosa a la base de datos")
        # Aquí puedes ejecutar consultas o realizar otras operaciones

        # Cierra la conexión
        conn.close()
    else:
        print("No se pudo conectar a la base de datos")

except mysql.connector.Error as e:
    print(f"Error de conexión: {e}")
