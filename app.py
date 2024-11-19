from flask import Flask, render_template, request, redirect, url_for
from controllers.controller import Controller
from models.heladeria import Heladeria
from models.copa import Copa
from models.malteada import Malteada

app = Flask(__name__, template_folder='views')

# Crear una instancia de Heladeria y Controller
heladeria = Heladeria()
controller = Controller(heladeria)

@app.route('/')
def index():
    # Obtener la información de los productos
    productos = controller.ver_productos()
    return render_template('index.html', productos=productos)

@app.route('/agregar_producto', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        tipo = request.form['tipo']
        ingredientes = []
        for i in range(3):
            nombre_ingrediente = request.form[f'nombre_ingrediente_{i+1}']
            precio_ingrediente = float(request.form[f'precio_ingrediente_{i+1}'])
            calorias_ingrediente = int(request.form[f'calorias_ingrediente_{i+1}'])
            ingredientes.append({"nombre": nombre_ingrediente, "precio": precio_ingrediente, "calorias": calorias_ingrediente})
        if tipo.lower() == "copa":
            tipo_vaso = request.form['tipo_vaso']
            producto = Copa(nombre, precio, tipo_vaso, ingredientes)
        elif tipo.lower() == "malteada":
            volumen = int(request.form['volumen'])
            producto = Malteada(nombre, precio, volumen, ingredientes)
        else:
            return "Tipo de producto inválido."
        controller.agregar_producto(producto)
        return redirect(url_for('index'))
    return render_template('agregar_producto.html')

@app.route('/vender_producto', methods=['GET', 'POST'])
def vender_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        if controller.vender_producto(nombre):
            return redirect(url_for('index'))
        else:
            return "Producto no disponible."
    return render_template('vender_producto.html')

@app.route('/ver_inventario')
def ver_inventario():
    inventario = controller.ver_inventario()
    return render_template('ver_inventario.html', inventario=inventario)

@app.route('/calcular_ganancias')
def calcular_ganancias():
    ganancias = controller.calcular_ganancias()
    return render_template('calcular_ganancias.html', ganancias=ganancias)

@app.route('/producto_mas_rentable')
def producto_mas_rentable():
    producto_rentable = controller.producto_mas_rentable()
    return render_template('producto_mas_rentable.html', producto_rentable=producto_rentable)

if __name__ == '__main__':
    app.run(debug=True)