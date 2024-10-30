import mysql.connector
from tkinter import *
from tkinter import messagebox

def ModificarUsuarios(self, root2):
    self.root2 = root2
    try:
        connection = mysql.connector.connect(
            host="bimtfzdinglabpw1yzd0-mysql.services.clever-cloud.com",
            user="u0ioaiitne1nh02w",
            passwd="svvGffwj1FHbLpuwy3UL",
            db="bimtfzdinglabpw1yzd0",
            port=3306,
        )
        cursor = connection.cursor()
    except mysql.connector.Error as err:
        return messagebox.showerror(
            message=f"Error de conexión: {err}", title="Mensaje"
        )

    cedula = self.cedula_agregar.get()
    nuevo_usuario = self.nuevo_usuario_agregar.get()
    nueva_clave = self.nueva_clave_agregar.get()
    tipo_cuenta = self.tipo_cuenta.get()

    if len(cedula) < 7:
        messagebox.showerror("Error", "La cédula debe tener más de 6 dígitos")
        return

    if len(nuevo_usuario) < 6 or len(nueva_clave) < 6:
        messagebox.showerror("Error", "Datos muy cortos, No Validos")
        return

    cursor.execute("SELECT Cedula, id_RolUsuario FROM usuarios WHERE Cedula = %s", (cedula,))
    resultado_busqueda = cursor.fetchone()

    if resultado_busqueda:
        if resultado_busqueda[1] == 1:
            messagebox.showerror("Error", "No se puede modificar la cuenta del sistema")
            return

        cursor.execute("SELECT COUNT(*) FROM usuarios WHERE id_RolUsuario = '2'")
        num_admins = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM usuarios WHERE id_RolUsuario = '3'")
        num_empleados = cursor.fetchone()[0]

        if tipo_cuenta == "2" and num_admins >= 2:
            messagebox.showerror("Error", "No se pueden registrar más de 2 administradores.")
            return

        if tipo_cuenta == "3" and num_empleados >= 6:
            messagebox.showerror("Error", "No se pueden registrar más de 6 empleados.")
            return

        messagebox.showinfo(
            message="Cédula identificada correctamente", title="Mensaje"
        )

        try:
            cursor.execute(
                "UPDATE usuarios SET Cuenta = %s, Clave = %s, id_RolUsuario = %s WHERE Cedula = %s",
                (nuevo_usuario, nueva_clave, tipo_cuenta, cedula),
            )
            connection.commit()
            messagebox.showinfo(
                "Mensaje", "Excelente, datos actualizados correctamente"
            )
            self.root2.destroy()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", "No se pudieron actualizar los datos")
            print(f"Error al actualizar los datos: {e}")
    else:
        messagebox.showerror(
            message="Cédula no encontrada. Verifica nuevamente", title="Mensaje"
        )

    connection.close()
