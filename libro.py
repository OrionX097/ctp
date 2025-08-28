class Libro:
    def __init__(self,titulo,autor,genero_literario,cantidad_hojas):
        self.titulo = titulo
        self.autor= autor
        self.genero_literario = genero_literario
        self.cantidad_hojas = cantidad_hojas
        
    def infomacion(self):
        print("-------------INFORMACION-------------")
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Genero literario: {self.genero_literario}")
        print(f"Cantidad de hojas: {self.cantidad_hojas}")
        
libro_jp = Libro()

libro_jp.infomacion()