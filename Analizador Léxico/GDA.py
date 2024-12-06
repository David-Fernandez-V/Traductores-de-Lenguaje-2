class GDA:
    def __init__(self):
        self.nodos = []

    def insertar_nodo(self,etiqueta,argumento1,argumento2):
        nodo = (etiqueta,argumento1,argumento2)
        if nodo in self.nodos:
            return self.nodos.index(nodo)
        else:
            print("Nuevo nodo: ",etiqueta,",",argumento1,",",argumento2)
            self.nodos.append(nodo)
            return len(self.nodos) - 1

    def obtener_longitud(self):
        return len(self.nodos)
    
    def limpiar_elementos(self):
        self.nodos.clear()
