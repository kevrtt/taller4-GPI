import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Cargar los datos
data = pd.read_csv('proyecto/data/raw/synthetic_data.csv')

# Definir las variables predictoras (X) y la variable objetivo (y)
X = data[['Age']]  # Usamos la Edad como variable predictora
y = data['Salary']  # Usamos el Salario como la variable objetivo

# Crear el modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo
model.fit(X, y)

# Realizar predicciones
y_pred = model.predict(X)

# Visualizar los resultados
plt.scatter(X, y, color='blue', alpha=0.5, label='Datos reales')
plt.plot(X, y_pred, color='red', label='Modelo de regresión')
plt.title('Regresión Lineal: Edad vs Salario')
plt.xlabel('Edad')
plt.ylabel('Salario (USD)')
plt.legend()
plt.grid(True)
plt.show()

# Guardar los coeficientes y el modelo
print(f'Coeficiente de la regresión: {model.coef_}')
print(f'Intersección de la regresión: {model.intercept_}')

# Guardar las predicciones en un archivo CSV
predictions = pd.DataFrame({
    'Age': X['Age'],
    'Predicted_Salary': y_pred
})
predictions.to_csv('proyecto/results/tables/linear_regression_predictions.csv', index=False)
