from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas

def generar_pdf(datos):
    c = canvas.Canvas("mi_archivo.pdf", pagesize=landscape(letter))
    
    # Título del formulario
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 550, "Formulario de Servicio")

    # Datos del cliente
    c.setFont("Helvetica", 12)
    c.drawString(50, 500, "Nombre del Cliente: " + datos["nombre"])
    c.drawString(50, 480, "Dirección: " + datos["direccion"])
    c.drawString(50, 460, "Teléfono: " + datos["telefono"])
    c.drawString(50, 440, "Fecha de Orden: " + datos["fecha_orden"])

    # Datos del equipo
    c.drawString(50, 400, "Modelo de Equipo: " + datos["modelo_equipo"])
    c.drawString(50, 380, "Marca del Equipo: " + datos["marca_equipo"])

    # Sección de descripción del servicio
    c.drawString(50, 340, "Descripción del Servicio:")
    c.drawString(50, 320, datos["descripcion_servicio"])

    # Sección de observaciones
    c.drawString(50, 280, "Observaciones:")
    c.drawString(50, 260, datos["observaciones"])

    # Firma del cliente
    c.drawString(50, 220, "Firma del Cliente: __________________________")

    # Firma del técnico
    c.drawString(50, 200, "Firma del Técnico: __________________________")

    c.save()

if __name__ == "__main__":
    datos_usuario = {
        "nombre": "Juan Pérez",
        "direccion": "Calle Falsa 123",
        "telefono": "123456789",
        "fecha_orden": "12/09/2024",
        "modelo_equipo": "Laptop XYZ",
        "marca_equipo": "Marca ABC",
        "descripcion_servicio": "Reparación de pantalla y actualización de software.",
        "observaciones": "Ninguna."
    }
    generar_pdf(datos_usuario)
    print("PDF generado exitosamente.")
