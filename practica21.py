class Vehiculo():
    def __init__(self,marca,modelo,capacidad):
        self.marca = marca
        self.modelo = modelo
        self.capacidad = capacidad
    
class Colectivo(Vehiculo):
    def __init__(self,marca,modelo,capacidad,recorrido):
        super().__init__(marca,modelo,capacidad)
        self.recorrido = recorrido
    
    def parar_en_parada(self):
        print(f"El colectivo de la linea {self.recorrido} está parando en la parada.")

class Taxi(Vehiculo):
    def __init__(self,marca,modelo,capacidad):
        super().__init__(marca,modelo,capacidad)
        self.tarifa = 40
    
    def cobrar_viaje(self):
        distancia = int(input("Ingrese la cantidad de kilometros que viajara:"))
        precio_total= distancia * self.tarifa
        print(f"El pasajero del auto {self.marca} {self.modelo} debe pagar {precio_total}")

class Avion(Vehiculo):
    def __init__(self,marca,modelo,capacidad,aerolinea):
        super().__init__(marca,modelo,capacidad)
        self.aerolinea = aerolinea

    def despegar(self):
        print(f"El avion {self.marca} {self.modelo} de la aerolinea {self.aerolinea} esta despegando.")


mi_cole=Colectivo("Iveco","T32",50,"C210")
mi_cole.parar_en_parada()

mi_taxi=Taxi("Renault","12",4)
mi_taxi.cobrar_viaje()

mi_avion=Avion("Gauss","L100",200,"Papuaerolineas")
mi_avion.despegar()
