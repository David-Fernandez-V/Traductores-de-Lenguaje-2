class TablaSimbolos:
    def __init__(self):
        self.simbolos = []

    def insertar_simbolo(self, simbolo):
        if simbolo in self.simbolos:
            return self.simbolos.index(simbolo)
        else:
            print("Nuevo simbolo: ",simbolo)
            self.simbolos.append(simbolo)
            return len(self.simbolos) - 1

    def obtener_longitud(self):
        return len(self.simbolos)
    
    def limpiar_elementos(self):
        self.simbolos.clear()