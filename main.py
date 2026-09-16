from negocio import Negocio
from interfaz import menu


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



