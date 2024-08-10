import pandas as pd

# Datos de ejemplo
data = {
    'Cliente': ['A', 'A', 'B', 'C', 'B', 'C', 'A', 'B', 'C', 'A'],
    'Producto': ['Manzanas', 'Plátanos', 'Yogurt', 'Manzanas', 'Yogurt', 'Plátanos', 'Yogurt', 'Manzanas', 'Plátanos', 'Yogurt']
}

df = pd.DataFrame(data)
print("Datos de compras:\n", df)
from collections import Counter

# Calcular frecuencia de compra de cada producto
productos_populares = dict(Counter(df['Producto']))

# Ordenar los productos por frecuencia de compra
productos_recomendados = sorted(productos_populares, key=productos_populares.get, reverse=True)

print("Productos recomendados basados en popularidad:")
for producto in productos_recomendados:
    print(producto)
