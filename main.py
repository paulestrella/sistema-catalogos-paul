catalogo_negocio = [
    {"nombre": "Masaje corporales", "precio": 500.00, "disponibilidad": True},
    {"nombre": "Manicure", "precio": 200.00, "disponibilidad": True},
    {"nombre": "Pedicure", "precio": 300.00, "disponibilidad": False}
]


def main():
    while True:
        print("0. Salir")
        opcion = input("Elige una opcion: ")

        if opcion == "0":
            print("Hasta luego!")
            break


if __name__ == "__main__":
    main()
