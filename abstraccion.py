
#      ABSTRACCIÓN

def calcular_subtotal(precio, cantidad):
    return precio * cantidad

def calcular_impuesto(subtotal):
    return subtotal * 0.12

def generar_factura(producto, precio, cantidad):
    # Función principal que abstrae todo el proceso
    subtotal = calcular_subtotal(precio, cantidad)
    impuesto = calcular_impuesto(subtotal)
    total = subtotal + impuesto

    return f"""
    --- FACTURA ---
    Producto: {producto}
    Cantidad: {cantidad}
    Precio Unitario: ${precio}
    Subtotal: ${subtotal}
    Impuesto (12%): ${impuesto}
    Total a pagar: ${total}
    """

print("=== ABSTRACCIÓN ===")
print(generar_factura("Hamburguesa", 5.50, 4))
