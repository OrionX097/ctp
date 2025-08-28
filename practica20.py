#Hecho por Juan Pablo Sifuente,Tomas Rodriguez y Orion Barrionuevo.
class Show:
    def __init__(self,artista,fecha,entradas,info):
        self.artista = artista
        self.fecha = fecha
        self.entradas = entradas
        self.info = info
    
    def mostrar_info(self):
        print(f"Quedan {self.entradas} entradas")
    
    
class Cliente:
    def __init__(self,nombre):
        self.nombre = nombre
        self.cantidad_entrada = 0

    def compra_entrada(self,cantidad,show):
        if show.entradas >= cantidad:
            print(f"se realizo el pago de {self.nombre} ")
            
            show.entradas -= cantidad
            self.cantidad_entrada += cantidad
            print(f"ahora hay {show.entradas} entradas disponibles de {show.artista}")
        else:
            print(f"no se pudo realizar el pago de {self.nombre}")
            print(f"no hay entradas suficientes, solo hay {show.entradas}")
        
    def mostrar(self):
        print(f"{self.nombre} tiene la cantidad total de entradas compradas de {self.cantidad_entrada}")

tussiwariors = Show("tussiwariors", "11/9/2001", 5,"no pasa tonkas")
kendrick = Show("kendri", "11/9/2007", 9,"no pasa tonkas")

tincho = Cliente("tincho")
jp= Cliente("Jp")

tincho.compra_entrada(2,tussiwariors)
tincho.compra_entrada(3, kendrick)
tincho.mostrar()
jp.compra_entrada(3000000,tussiwariors)


