class Celular:
    def __init__(self, marca, modelo, almacenamiento):
        self.marca = marca
        self.modelo = modelo
        self.almacenamiento = almacenamiento
        self.encendido = False
    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo} está encendido.")
        else:
            print("El celular ya estaba encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print("El celular se apagó.")
        else:
            print("El celular ya estaba apagado.")

mi_celu= Celular("Samsung","Galaxy A10",64)

mi_celu.encender()

mi_celu.apagar()
