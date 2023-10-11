import time

class Fiboiter():
    #todos los parametros(def) de clase en python necesitan self para existir
    #para inicializar cosas dentro de la clase se utiliza def __init__()
    def __init__(self, max= None):
        self.max = max
    
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.cont = 0
        return self
    
    def __next__(self):
        if not self.max:
            if self.cont == 0:
                self.cont += 1
                return self.n1
            elif self.cont == 1:
                self.cont += 1
                return self.n2
            else:
                self.aux = self.n1 + self.n2
                #self.n1 = self.n2
                #self.n2 = self.aux
                #ejemplo de suaping, intercambiar valor igual que arriba
                self.n1, self.n2 = self.n2, self.aux
                self.cont += 1
                return self.aux
        else:
            if self.cont == 0:
                self.cont += 1
                return self.n1
            elif self.cont == 1:
                self.cont += 1
                return self.n2
            else:
                self.aux = self.n1 + self.n2
                self.n1, self.n2 = self.n2, self.aux
                if self.aux >= self.max + 1:
                    raise StopIteration
                self.cont += 1
                return self.aux
        
if __name__ == "__main__":
    fibonacci = Fiboiter(98)
    for element in fibonacci:
        print(element)
        time.sleep(1)#pausa la ejecucion del programa 1 segundo