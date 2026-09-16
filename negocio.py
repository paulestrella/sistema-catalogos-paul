class Negocio:
	def __init__(self, catalogo):
		self.catalogo = catalogo

	def ver_catalogo(self):
		for producto in self.catalogo:
			print(f"{producto['nombre']}: ${producto['precio']}")

	def buscar_producto(self, nombre_buscado):
		nombre_normalizado = nombre_buscado.strip().lower()
		for producto in self.catalogo:
			nombre_producto = producto["nombre"].strip().lower()
			if nombre_producto == nombre_normalizado:
				return producto
		return None

	def agregar_producto(self, nombre, precio, disponible):
		try:
			precio_numero = float(precio)
		except ValueError:
			print("El precio debe ser un numero. Producto no agregado")
			return None

		nuevo_producto = {
			"nombre": nombre,
			"precio": precio_numero,
			"disponibilidad": disponible
		}
		self.catalogo.append(nuevo_producto)
		return nuevo_producto

	def producto_disponible(self):
		productos_disponibles = []
		for producto in self.catalogo:
			if producto["disponibilidad"] is True:
				productos_disponibles.append(producto)
		return productos_disponibles
