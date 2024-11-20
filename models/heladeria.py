from sqlalchemy.orm import sessionmaker
from database import engine, Copa, Malteada, Ingrediente

Session = sessionmaker(bind=engine)
session = Session()

class Heladeria:
    def __init__(self):
        self.productos = []
        self.ingredientes = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        session.add(producto)
        session.commit()

    def vender_producto(self, nombre):
        # Buscar el producto (Copa o Malteada) por nombre
        producto = session.query(Copa).filter_by(nombre=nombre).first() or session.query(Malteada).filter_by(nombre=nombre).first()
        
        if producto:
            # Verificar los ingredientes del producto en el inventario
            ingredientes_faltantes = []
            for ingrediente in [producto.ingrediente_1, producto.ingrediente_2, producto.ingrediente_3]:
                if not session.query(Ingrediente).filter_by(nombre=ingrediente).first():
                    ingredientes_faltantes.append(ingrediente)

            if ingredientes_faltantes:
                # Si faltan ingredientes, lanzar un ValueError con el nombre del ingrediente faltante
                raise ValueError(f"¡Oh no! Nos hemos quedado sin {' y '.join(ingredientes_faltantes)}")

            # Si todo está bien, realizar la venta
            self.productos.remove(producto)
            session.delete(producto)
            session.commit()
            return "¡Vendido!"
        
        return "Producto no encontrado."

    def ver_inventario(self):
        return {ingrediente.nombre: ingrediente for ingrediente in session.query(Ingrediente).all()}

    def ver_productos(self):
        return session.query(Copa).all() + session.query(Malteada).all()

    def calcular_ganancias(self):
        return sum(producto.precio_publico for producto in self.productos)

    def producto_mas_rentable(self):
        productos = session.query(Copa).all() + session.query(Malteada).all()
        if not productos:
            return None
        return max(productos, key=lambda p: p.precio_publico - sum(i.precio for i in [p.ingrediente_1, p.ingrediente_2, p.ingrediente_3]))
