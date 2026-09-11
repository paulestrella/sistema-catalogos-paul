class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

Luis = Persona("Luis")
Manuel = Persona("Manuel")

Luis.saludar()
Manuel.saludar()