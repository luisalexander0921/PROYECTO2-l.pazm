from models.heladeria import Heladeria

class Controller:
    def __init__(self, heladeria: Heladeria):
        self.heladeria = heladeria

    def agregar_producto(self, producto):
        self.heladeria.agregar_producto(producto)

    def vender_producto(self, nombre):
        return self.heladeria.vender_producto(nombre)

    def ver_inventario(self):
        return self.heladeria.ver_inventario()

    def ver_productos(self):
        return self.heladeria.ver_productos()

    def calcular_ganancias(self):
        return self.heladeria.calcular_ganancias()

    def producto_mas_rentable(self):
        return self.heladeria.producto_mas_rentable()