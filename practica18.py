class Auto:
    def __init__(self,combustible):
        self.combustible = combustible

    def info_combustible(self):
        print(f"hay {self.combustible} de combustible")

class Conductor:
    def __init__(self,nombre):
        self.nombre = nombre
    
    def mostrar_nombre (self):
        print(f"Nombre de conductor:{self.nombre}")

    def manejar(self,litros,auto):
        if auto.combustible >= litros:
            auto.combustible -= litros
            print(f"{self.nombre} gasto {litros}L y quedo {auto.combustible}")
        else:
            print(f"El auto no tiene combustible suficiente, tiene {auto.combustible}")


miauto= Auto(40)
conductor= Conductor("pepito")
conductor.manejar(20,miauto)
