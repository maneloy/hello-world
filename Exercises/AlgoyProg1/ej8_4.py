lista_productos = [(0, 'Pollo', 30), (1, 'Pescado', 40), (2, 'Salame', 15), (3, 'Caramelos', 5), (4, 'Espuma de afeitar', 100), (5, 'Juguete', 50), (6, 'Sandía', 60), (7, 'Queso', 25), (8, 'Yogurt', 6)]

productos_a_facturar = [(2, 4), (5, 2), (7, 1), (4, 6), (8,3)]

def facturar(productos, a_facturar):
	total_general = 0
	for produc in a_facturar:
		precio_unitario = productos[produc[0]][2]
		precio_total = precio_unitario * produc[1]
		descripcion = productos[produc[0]][1]
		cantidad = produc[1]
		total_general += precio_total
		print("Descripción: {} | Cantidad: {} | Precio_unitario: ${} | Precio_total: ${}".format(descripcion, cantidad, precio_unitario, precio_total))
	print("Total general: ${}".format(total_general))

facturar(lista_productos, productos_a_facturar) #Prueba