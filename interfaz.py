def menu(negocio):
	while True:
		print("0. Salir")
		print("1. Ver catalogo completo")
		print("2. Buscar un producto")
		print("3. Agregar un producto nuevo")
		print("4. Ver solo los productos disponibles")
		opcion = input("Elige una opcion: ")

		if opcion == "0":
			print("Hasta luego!")
			break

		elif opcion == "1":
			negocio.ver_catalogo()

		elif opcion == "2":
			nombre = input("Ingrese el nombre del producto: ")
			producto = negocio.buscar_producto(nombre)
			if producto is not None:
				print(f"{producto['nombre']}: ${producto['precio']}")
			else:
				print("producto no encontrado")

		elif opcion == "3":
			nombre = input("Ingrese el nombre del producto: ")
			precio = input("Ingrese el precio del producto: ")
			producto = negocio.agregar_producto(nombre, precio, True)
			if producto is not None:
				print(f"Se agrego el producto: {producto['nombre']} - ${producto['precio']}")

		elif opcion == "4":
			productos = negocio.producto_disponible()
			for producto in productos:
				print(f"{producto['nombre']}: ${producto['precio']}")


if __name__ == "__main__":
	menu()