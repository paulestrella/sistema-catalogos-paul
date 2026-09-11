catalogo_negocio = [
    {"nombre": "Masaje corporales", "precio": 500.00, "disponibilidad": True},
    {"nombre": "Manicure", "precio": 200.00, "disponibilidad": True},
    {"nombre": "Pedicure", "precio": 300.00, "disponibilidad": False}
]


class Negocio:
    def __init__(self, catalogo):
        self.catalogo = catalogo

    def ver_catalogo(self):
        for producto in self.catalogo:
            print(f"{producto['nombre']}: ${producto['precio']}")


def buscar_producto(catalogo, nombre_buscado):
    for producto in catalogo:
        if producto["nombre"].lower() == nombre_buscado.lower():
            return producto
    return None


def agregar_producto(catalogo, nombre, precio, disponible):
    nuevo_producto = {
        "nombre": nombre,
        "precio": precio,
        "disponibilidad": disponible
    }
    catalogo.append(nuevo_producto)
    return nuevo_producto


def producto_disponible(catalogo, disponible=None):
    if disponible is not None:
        productos_disponibles = []
        for producto in catalogo:
            if producto["disponibilidad"] == disponible:
                productos_disponibles.append(producto)
        return productos_disponibles

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
            for producto in catalogo_negocio:
                print(f"{producto['nombre']}: ${producto['precio']}")

        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto: ")
            producto = buscar_producto(catalogo_negocio, nombre)
            if producto is not None:
                print(f"{producto['nombre']}: ${producto['precio']}")
            else:
                print("producto no encontrado")

        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            disponible = True
            producto = agregar_producto(catalogo_negocio, nombre, precio, disponible)
            print(f"Se agrego el producto: {producto['nombre']} - ${producto['precio']}")

        elif opcion == "4":
            productos = producto_disponible(catalogo_negocio, True)
            for producto in productos:
                print(f"{producto['nombre']}: ${producto['precio']}")


def main():
    producto_disponible(catalogo_negocio)


if __name__ == "__main__":
    main()



