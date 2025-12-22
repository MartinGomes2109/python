import pandas as pd
import matplotlib.pyplot as plt


def run():

    #cargar los datos del CSV
    data = pd.read_csv('ventas.csv')
    # Convertir la columna fecha a datetime
    data['fecha'] = pd.to_datetime(data['fecha'])
    print(data)

    #calcular ventas totales por mes
    data['mes'] = data['fecha'].dt.to_period('M')
    ventas_totales_por_mes = data.groupby('mes').apply(lambda x: (x['cantidad'] * x['precio']).sum())
    ventas_totales_por_mes = ventas_totales_por_mes.sort_index()
    print('Ventas totales por mes:')
    print(ventas_totales_por_mes)

    #determinar producto mas vendido
    data['ingreso'] = data['cantidad'] * data['precio']
    producto_mas_vendido = data.groupby('producto').agg({
        'cantidad': 'sum', 
        'ingreso': 'sum'
    })
    mas_vendido = producto_mas_vendido['cantidad'].idxmax()
    mayor_ingreso = producto_mas_vendido['ingreso'].idxmax()
    print(f'El producto mas vendido es {mas_vendido} (total {producto_mas_vendido.loc[mas_vendido, "cantidad"]} unidades)')
    print(f'El producto con mayor ingreso es {mayor_ingreso} (total {producto_mas_vendido.loc[mayor_ingreso, "ingreso"]:.2f} pesos)')

    #graficar ventas por mes
    ventas_totales_por_mes.index = ventas_totales_por_mes.index.astype(str)
    plt.figure(figsize=(6, 4))
    ventas_totales_por_mes.plot(kind='bar', color='skyblue')
    plt.title('Ventas por Mes')
    plt.xlabel('Mes')
    plt.ylabel('Ventas (pesos)')
    plt.tight_layout()
    plt.savefig('ventas_por_mes.png')
    plt.show()

    #graficar top 5 productos por mes
    top5 = producto_mas_vendido.nlargest(5, 'ingreso')
    plt.figure(figsize=(6, 4))
    plt.bar(top5.index, top5['ingreso'])
    plt.title('Top 5 Productos por Mes')
    plt.xlabel('Producto')
    plt.ylabel('Ventas (pesos)')
    plt.tight_layout()
    plt.savefig("top5_productos.png")
    plt.show()

if __name__ == '__main__':
    run()