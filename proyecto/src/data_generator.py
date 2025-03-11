import numpy as np
import pandas as pd

def generate_synthetic_data(n=1000):
    # Generar edades aleatorias entre 20 y 60
    ages = np.random.randint(20, 60, size=n)
    
    # Generar salarios aleatorios entre 30,000 y 100,000
    salaries = np.random.uniform(30000, 100000, size=n)
    
    # Crear un DataFrame con los datos generados
    data = pd.DataFrame({
        'Age': ages,
        'Salary': salaries
    })
    
    # Guardar los datos generados en un archivo CSV
    data.to_csv('proyecto/data/raw/synthetic_data.csv', index=False)
    print("Datos sintéticos generados y guardados en 'proyecto/data/raw/synthetic_data.csv'.")

# Llamar a la función para generar datos
if __name__ == "__main__":
    generate_synthetic_data()
