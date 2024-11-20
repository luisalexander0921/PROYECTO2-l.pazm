import unittest
from models.heladeria import Heladeria, Ingrediente, Copa, Malteada
from sqlalchemy.orm import sessionmaker
from database import engine

# Crear una sesión de base de datos en memoria para las pruebas
Session = sessionmaker(bind=engine)
session = Session()

class TestHeladeria(unittest.TestCase):
    def setUp(self):
        # Inicializar Heladería antes de cada prueba
        self.heladeria = Heladeria()
        
        # Crear algunos ingredientes de prueba
        self.ingrediente_chocolate = Ingrediente(nombre="Chocolate", sano=True, cantidad=10)
        self.ingrediente_vainilla = Ingrediente(nombre="Vainilla", sano=True, cantidad=5)
        session.add(self.ingrediente_chocolate)
        session.add(self.ingrediente_vainilla)
        session.commit()
        
        # Crear productos (Copa, Malteada) de prueba
        self.copa = Copa(nombre="Copa de Chocolate", precio_publico=5.0, ingrediente_1=self.ingrediente_chocolate)
        self.malteada = Malteada(nombre="Malteada de Vainilla", precio_publico=7.0, ingrediente_1=self.ingrediente_vainilla)
        session.add(self.copa)
        session.add(self.malteada)
        session.commit()

    def test_ingrediente_sano(self):
        # Probar si un ingrediente es sano
        self.assertTrue(self.ingrediente_chocolate.sano)
        self.assertTrue(self.ingrediente_vainilla.sano)

    def test_abastecer_ingrediente(self):
        # Probar si se puede abastecer un ingrediente
        self.ingrediente_chocolate.cantidad += 5
        session.commit()
        self.assertEqual(self.ingrediente_chocolate.cantidad, 15)

    def test_renovar_inventario(self):
        # Supongamos que renovar inventario aumenta la cantidad de ingredientes
        self.ingrediente_chocolate.cantidad += 10
        self.ingrediente_vainilla.cantidad += 10
        session.commit()
        self.assertEqual(self.ingrediente_chocolate.cantidad, 20)
        self.assertEqual(self.ingrediente_vainilla.cantidad, 15)

    def test_calcular_calorias_copa(self):
        # Calcular calorías de un producto Copa
        calorias = self.copa.calcular_calorias()  # Asume que este método está definido
        self.assertEqual(calorias, 200)  # Establecer valor esperado según la lógica del método

    def test_calcular_calorias_malteada(self):
        # Calcular calorías de un producto Malteada
        calorias = self.malteada.calcular_calorias()  # Asume que este método está definido
        self.assertEqual(calorias, 300)  # Establecer valor esperado según la lógica del método

    def test_calcular_costo_produccion(self):
        # Calcular el costo de producción de un producto
        costo = self.copa.calcular_costo_produccion()  # Asume que este método está definido
        self.assertEqual(costo, 2.0)  # Establecer valor esperado según la lógica del método

    def test_calcular_rentabilidad(self):
        # Calcular la rentabilidad de un producto
        rentabilidad = self.copa.calcular_rentabilidad()  # Asume que este método está definido
        self.assertEqual(rentabilidad, 3.0)  # Establecer valor esperado según la lógica del método

    def test_producto_mas_rentable(self):
        # Probar que se encuentra el producto más rentable
        producto_rentable = self.heladeria.producto_mas_rentable()
        self.assertEqual(producto_rentable.nombre, "Copa de Chocolate")  # Basado en la rentabilidad esperada

    def test_vender_producto_exitoso(self):
        # Vender un producto cuando está disponible
        resultado = self.heladeria.vender_producto("Copa de Chocolate")
        self.assertEqual(resultado, "¡Vendido!")

    def test_vender_producto_fallido(self):
        # Vender un producto que falta un ingrediente
        self.ingrediente_chocolate.cantidad = 0  # Simula que no hay suficiente ingrediente
        session.commit()
        with self.assertRaises(ValueError):
            self.heladeria.vender_producto("Copa de Chocolate")

    def test_vender_producto_ingrediente_faltante(self):
        # Verifica el mensaje de error cuando un ingrediente falta
        self.ingrediente_chocolate.cantidad = 0  # Simula que no hay suficiente ingrediente
        session.commit()
        try:
            self.heladeria.vender_producto("Copa de Chocolate")
        except ValueError as e:
            self.assertEqual(str(e), "¡Oh no! Nos hemos quedado sin Chocolate")

    def tearDown(self):
        # Limpiar después de cada prueba
        session.query(Copa).delete()
        session.query(Malteada).delete()
        session.query(Ingrediente).delete()
        session.commit()


if __name__ == '__main__':
    unittest.main()
