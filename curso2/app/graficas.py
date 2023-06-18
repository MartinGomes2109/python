import matplotlib.pyplot as plt

def generar_grafica_bar(labels,values):
    
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.show()
    
def generar_grafica_pie(labels,values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()
    
if __name__ == '__main__':
    labels = ['a','b','c']
    values = [100,150,200]
    generar_grafica_bar(labels, values)
    generar_grafica_pie(labels,values)
    #primero se va a ejecutar la grafica char, al cerrar la ventana de la primera grafica se va a ejecutar la siguiente
    #control+c interrumpir accion en la terminal