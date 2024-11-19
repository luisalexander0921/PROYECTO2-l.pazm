# Punto 1 | ¿Esto es Sano?
def es_sano(calorias: int, es_vegetariano: bool) -> bool:
    return calorias < 100 or es_vegetariano

# Punto 2 | Las Calorías
def calorias(calorias_ingrediente: list) -> float:
    total_calorias = sum(calorias_ingrediente)
    total_calorias_con_descuento = total_calorias * 0.95
    return round(total_calorias_con_descuento, 2)

# Punto 3 | Costos
def costo_producto(ingrediente_1: dict, ingrediente_2: dict, ingrediente_3: dict) -> float:
    costo_total = ingrediente_1["precio"] + ingrediente_2["precio"] + ingrediente_3["precio"]
    return costo_total

# Punto 4 | Rentabilidad
def rentabilidad_producto(precio_producto: float, ingrediente_1: dict, ingrediente_2: dict, ingrediente_3: dict) -> float:
    rentabilidad = precio_producto - (ingrediente_1["precio"] + ingrediente_2["precio"] + ingrediente_3["precio"])
    return rentabilidad

# Punto 5 | El mejor producto
def mejor_producto(producto_1: dict, producto_2: dict, producto_3: dict, producto_4: dict) -> dict:
    productos = [producto_1, producto_2, producto_3, producto_4]
    producto_rentable = max(productos, key=lambda x: x["rentabilidad"])
    return producto_rentable