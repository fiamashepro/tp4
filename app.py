from datetime import datetime
import streamlit as st
import calculos
import mi_negocio
import pdf_presupuesto

st.title(f"Presupuesto - {mi_negocio.NOMBRE_NEGOCIO}")



cliente = st.text_input("Nombre del cliente:")
forma_pago = st.selectbox("Forma de pago:", [calculos.EFECTIVO, calculos.TRANSFERENCIA])

nombres = []
cantidades = []
precios_unitarios = []

st.subheader("Productos")


for i in range(len(mi_negocio.productos)):
    nombre_prod = mi_negocio.productos[i]
    precio_prod = mi_negocio.precios[i]
    
    cant = st.number_input(
        label=f"{nombre_prod} (${precio_prod:.2f})", 
        min_value=0, 
        value=0, 
        step=1, 
        key=f"prod_{i}"
    )
    
    if cant > 0:
        nombres.append(nombre_prod)
        cantidades.append(cant)
        precios_unitarios.append(precio_prod)

#descarga de PDF
if len(cantidades) > 0:
    subtotal = calculos.calcular_subtotal(cantidades, precios_unitarios)
    descuento = calculos.calcular_descuento(subtotal, forma_pago)
    monto_desc = subtotal - descuento
    iva = calculos.calcular_iva(monto_desc)
    total = calculos.calcular_total(subtotal, descuento, iva)

    st.subheader("Resumen")
    st.write(f"Subtotal: ${subtotal:.2f}")
    st.write(f"Descuento: ${descuento:.2f}")
    st.write(f"IVA: ${iva:.2f}")
    st.write(f"TOTAL: ${total:.2f}")

    if cliente.strip() == "":
        st.warning("Ingrese el nombre del cliente para descargar el PDF.")
    else:
        fecha = datetime.now().strftime("%d/%m/%Y")
        pdf_bytes = pdf_presupuesto.generar_pdf(
            mi_negocio.NOMBRE_NEGOCIO,
            mi_negocio.RUBRO,
            cliente,
            fecha,
            nombres,
            cantidades,
            precios_unitarios,
            subtotal,
            descuento,
            iva,
            total,
            forma_pago
        )
        st.download_button("Descargar PDF", data=pdf_bytes, file_name="presupuesto.pdf")
else:
    st.info("Seleccione al menos un producto con cantidad mayor a 0.")