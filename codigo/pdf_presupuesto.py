import os
from fpdf import FPDF

def generar_pdf(nombre_negocio, rubro, cliente, fecha, nombres, cantidades, precios, subtotal, descuento, iva, total, forma_pago):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # LOGO: Carga logo.jpg (la foca) o logo.png si existe
    if os.path.exists("logo.jpg"):
        pdf.image("logo.jpg", x=15, y=15, w=30)
    elif os.path.exists("logo.png"):
        pdf.image("logo.png", x=15, y=15, w=30)

    # ENCABEZADO SUPERIOR DERECHO
    pdf.set_xy(90, 15)
    pdf.set_font("helvetica", "B", 18)
    pdf.cell(105, 8, str(nombre_negocio), 0, 1, "R")
    
    pdf.set_font("helvetica", "", 10)
    pdf.cell(0, 5, "Presupuesto N° 1", 0, 1, "R")
    pdf.cell(0, 5, f"Fecha: {fecha}", 0, 1, "R")
    
    pdf.ln(22)
    
    # DATOS DEL CLIENTE
    pdf.set_font("helvetica", "", 11)
    pdf.cell(100, 7, "Cliente", 0, 0, "L")
    pdf.cell(95, 7, str(cliente), 0, 1, "R")
    pdf.ln(2)
    
    # LISTADO DE PRODUCTOS
    for i in range(len(nombres)):
        prod_str = f"{cantidades[i]} x {nombres[i]}"
        precio_str = f"${precios[i]:.2f} c/u"
        pdf.cell(100, 7, prod_str, 0, 0, "L")
        pdf.cell(95, 7, precio_str, 0, 1, "R")
        
    pdf.ln(6)
    
    # SUBTOTALES Y TOTAL
    pdf.cell(100, 7, "Subtotal", 0, 0, "L")
    pdf.cell(95, 7, f"${subtotal:.2f}", 0, 1, "R")
    
    pdf.cell(100, 7, "Descuento", 0, 0, "L")
    pdf.cell(95, 7, f"-${descuento:.2f}", 0, 1, "R")
    
    pdf.cell(100, 7, "IVA 21%", 0, 0, "L")
    pdf.cell(95, 7, f"${iva:.2f}", 0, 1, "R")
    
    pdf.ln(2)
    pdf.set_font("helvetica", "B", 13)
    pdf.cell(100, 8, "TOTAL", 0, 0, "L")
    pdf.cell(95, 8, f"${total:.2f}", 0, 1, "R")
    
    pdf.ln(20)
    
    # PIE DE PÁGINA
    pdf.set_font("helvetica", "I", 9)
    pdf.cell(0, 5, "Presupuesto válido por 7 días.", 0, 1, "L")
    
    return bytes(pdf.output())