class Tripletas:
    def __init__(self):
        self.tripltes = []

    def insertar_triplete(self,operacion,argumento1,argumento2):
        triplete = (operacion,argumento1,argumento2)
        
        if triplete in self.tripltes:
            return "(" + str(self.tripltes.index(triplete)) + ")"
        else:
            print(len(self.tripltes)," : ",operacion,",",argumento1,",",argumento2)
            self.tripltes.append(triplete)
            return "(" + str(len(self.tripltes) - 1) + ")"

    def obtener_longitud(self):
        return len(self.tripltes)
    
    def limpiar_elementos(self):
        self.tripltes.clear()
