from fpdf import FPDF

def generar_pdf(nombre_negocio, rubro, cliente, fecha, nombres, cantidades, precios, subtotal, descuento, iva, total, forma_pago):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "", 12)
    
    pdf.cell(0, 8, f"Negocio: {nombre_negocio} ({rubro})", 0, 1)
    pdf.cell(0, 8, f"Cliente: {cliente}", 0, 1)
    pdf.cell(0, 8, f"Fecha: {fecha}", 0, 1)
    pdf.cell(0, 8, f"Forma de pago: {forma_pago}", 0, 1)
    pdf.ln(5)
    
    pdf.cell(80, 8, "Producto", 1)
    pdf.cell(20, 8, "Cant", 1, 0, "C")
    pdf.cell(40, 8, "P. Unitario", 1, 0, "R")
    pdf.cell(40, 8, "Importe", 1, 1, "R")
    
    for i in range(len(nombres)):
        imp = cantidades[i] * precios[i]
        pdf.cell(80, 8, str(nombres[i]), 1)
        pdf.cell(20, 8, str(cantidades[i]), 1, 0, "C")
        pdf.cell(40, 8, f"${precios[i]:.2f}", 1, 0, "R")
        pdf.cell(40, 8, f"${imp:.2f}", 1, 1, "R")
        
    pdf.ln(5)
    pdf.cell(140, 6, f"Subtotal: ${subtotal:.2f}", 0, 1, "R")
    pdf.cell(140, 6, f"Descuento: -${descuento:.2f}", 0, 1, "R")
    pdf.cell(140, 6, f"IVA (21%): +${iva:.2f}", 0, 1, "R")
    pdf.cell(140, 6, f"TOTAL: ${total:.2f}", 0, 1, "R")
    
    return bytes(pdf.output())