import pandas as pd
import matplotlib.pyplot as plt

def visualize_data():
    # Cargar los datos generados
    data = pd.read_csv('proyecto/data/raw/synthetic_data.csv')
    
    # Crear un gráfico de dispersión entre Edad y Salario
    plt.figure(figsize=(8, 6))
    plt.scatter(data['Age'], data['Salary'], alpha=0.5, color='red')
    plt.title('Relación entre Edad y Salario')
    plt.xlabel('Edad')
    plt.ylabel('Salario (USD)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    visualize_data()
