import sqlite3 as SQL
connection = SQL.connect("SQLite\Registro.db")
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Usuarios (
                     id_Usuarios INTEGER PRIMARY KEY AUTOINCREMENT,
                     id_RolUsuario INTEGER,
                     Usuario TEXT,
                     Clave TEXT,
                     FOREIGN KEY(id_RolUsuario) REFERENCES RolUsuario(id_RolUsuario)
                )''')


cursor.execute('''CREATE TABLE IF NOT EXISTS RolUsuario (
                     id_RolUsuario INTEGER PRIMARY KEY AUTOINCREMENT,
                     NombreRol TEXT
               )''')


cursor.execute('''CREATE TABLE IF NOT EXISTS CambioTasa (
                     id_CambioTasa INTEGER PRIMARY KEY AUTOINCREMENT,
                     Tasa_Bol REAL,
                     Tasa_Cop REAL,
                     FechaTasa TEXT
               )''')

usuarios = [
    (1,'Tempus@Admin', 'TEMPUS09.'),
    (2,'Tempus@Empleado', 'TEMPUS09.'),
    (3,'Tempus@Backend', 'BACKEND')
]

for usuario in usuarios:
    cursor.execute("INSERT INTO Usuarios (id_RolUsuario, Usuario, Clave) VALUES (?,?,?)", usuario)
    
cursor.execute("INSERT INTO RolUsuario (NombreRol) VALUES ('Administrador')")
cursor.execute("INSERT INTO RolUsuario (NombreRol) VALUES ('Empleado')")
cursor.execute("INSERT INTO RolUsuario (NombreRol) VALUES ('Backend')")
    
connection.commit()