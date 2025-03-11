import pandas as pd

# Cargar los datos
data = pd.read_csv('proyecto/data/raw/synthetic_data.csv')

# Calcular estadísticas descriptivas
summary = data.describe()

# Imprimir el resumen
print(summary)

# Guardar el resumen en un archivo de texto
summary.to_csv('proyecto/results/tables/summary_statistics.csv', index=False)
