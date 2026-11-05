EFECTIVO = "Efectivo"
TRANSFERENCIA = "Transferencia"

def buscar_posicion(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

def calcular_subtotal(cantidades, precios):
    total = 0.0
    for i in range(len(cantidades)):
        total += cantidades[i] * precios[i]
    return round(total, 2)

def calcular_descuento(subtotal, forma_pago):
    if forma_pago == EFECTIVO:
        return round(subtotal * 0.10, 2)
    return 0.0

def calcular_iva(monto):
    return round(monto * 0.21, 2)

def calcular_total(subtotal, descuento, iva):
    return round((subtotal - descuento) + iva, 2)