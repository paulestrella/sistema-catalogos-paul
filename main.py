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


def main():
    catalogo_negocio = [
        {"nombre": "Masaje corporales", "precio": 500.00, "disponibilidad": True},
        {"nombre": "Manicure", "precio": 200.00, "disponibilidad": True},
        {"nombre": "Pedicure", "precio": 300.00, "disponibilidad": False}
    ]
    negocio = Negocio(catalogo_negocio)
    menu(negocio)


if __name__ == "__main__":
    main()



