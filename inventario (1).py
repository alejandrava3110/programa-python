def calcularPedido(stockActual, stockMinimo):
    if stockActual < stockMinimo:
        pedido = stockMinimo - stockActual
    else:
        pedido = 0
    return pedido

articulos = [
    [1001, "Lapicero", 5, 20],
    [1002, "Cuaderno", 50, 30],
    [1003, "Borrador", 200, 50],
    [1004, "Regla", 80, 25],
    [1005, "Tijeras", 30, 10]
]

print("LISTA DE PEDIDOS:")
print("--------------------")

for articulo in articulos:
    codigo = articulo[0]
    nombre = articulo[1]
    stockActual = articulo[2]
    stockMinimo = articulo[3]
    
    pedido = calcularPedido(stockActual, stockMinimo)
    
    print(f"Código: {codigo}, Artículo: {nombre}, Pedido: {pedido}")
    print("--------------------")