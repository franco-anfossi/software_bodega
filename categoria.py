
class Categoria:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.inventario = []

    def agregar_producto(self, producto):
        self.inventario.append(producto)

    def quitar_producto(self, producto):
        self.inventario.remove(producto)

    def buscar_producto(self, codigo):
        for producto in self.inventario:
            if producto.codigo == codigo:
                return producto
        return None

    def __str__(self):
        return f"{self.id} - {self.nombre}"