
class Bodega:
    def __init__(self, id):
        self.id = id
        self.categorias = {}

    def agregar_categoria(self, categoria):
        self.categorias[categoria.nombre] = categoria

    def quitar_categoria(self, categoria):
        del self.categorias[categoria.nombre]

    def buscar_categoria(self, nombre):
        return self.categorias.get(nombre)
    
    def __str__(self):
        text = f"Bodega {self.id}:\n"
        for categoria in self.categorias():
            text += f"{categoria}\n"