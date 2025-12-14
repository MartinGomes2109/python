import pandas as pd
import matplotlib.pyplot as plt


def run():
    data = pd.read_csv('/Users/martingomes/Documents/datos.csv', sep=';')
    print(data)
    print(f'\nForma del DataFrame: {data.shape}')
    print(f'Columnas: {data.columns.tolist()}')
    
    # Calcular la media de cada columna
    print('\n=== MEDIAS ===')
    medias = data.mean()
    print(medias)
    
    # Calcular la mediana de cada columna
    print('\n=== MEDIANAS ===')
    medianas = data.median()
    print(medianas)
    
    # Calcular la desviación estándar de cada columna
    print('\n=== DESVIACIÓN ESTÁNDAR ===')
    desviacion = data.std()
    print(desviacion)
    
    # Crear scatter plot de col1 vs col2
    print('\n=== CREANDO SCATTER PLOT ===')
    col1 = data.columns[0]  # Primera columna
    col2 = data.columns[1]  # Segunda columna
    
    plt.figure(figsize=(10, 6))
    plt.scatter(data[col1], data[col2], alpha=0.7, color='blue', s=50)
    plt.xlabel(f'{col1}')
    plt.ylabel(f'{col2}')
    plt.title(f'Scatter Plot: {col1} vs {col2}')
    plt.grid(True, alpha=0.3)
    plt.show()
    




if __name__ == '__main__':
    run()