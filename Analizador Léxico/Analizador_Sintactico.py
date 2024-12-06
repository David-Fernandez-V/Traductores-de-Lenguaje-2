from GDA import GDA
from Tabla_Simbolos import TablaSimbolos

FINAL_CADENA = ' '

class AnalizadorSintactico:
    def __init__(self):
        self.expresion = ''
        self.posicion_actual = 0
        self.es_expresion_valida = True
        self.tabla_simbolos = TablaSimbolos()
        self.gda = GDA()

    def set_expresion(self, expresion:str):
        self.expresion = expresion + FINAL_CADENA

    def invalidar_expresion(self):
        self.es_expresion_valida = False

    def validar_expresion(self):
        self.es_expresion_valida = True

    def reiniciar_posicion(self):
        self.posicion_actual = 0

    def get_preanalisis(self) -> str:
        return self.expresion[self.posicion_actual]

    def coincidir(self, caracter:str):
        if caracter ==  self.get_preanalisis():
            if(self.posicion_actual < len(self.expresion)-1):
                self.posicion_actual += 1
        else:
            self.invalidar_expresion()

    #Gramática
    def numero(self):
        num = ""
        preanalisis = self.get_preanalisis()
        while preanalisis.isdigit():
            num += preanalisis
            self.coincidir(preanalisis)
            preanalisis = self.get_preanalisis()
        if num:
            return num
        else:
            self.invalidar_expresion()
            return ""
    
    def identificador(self):
        id = ""
        preanalisis = self.get_preanalisis()
        if preanalisis.isalpha() or preanalisis == '_':
            id += preanalisis
            self.coincidir(preanalisis)
            preanalisis = self.get_preanalisis()
            
            while preanalisis.isalnum() or preanalisis == '_':
                id += preanalisis
                self.coincidir(preanalisis)
                preanalisis = self.get_preanalisis()
            posicion = self.tabla_simbolos.insertar_simbolo(id)
            return posicion
        else:
            self.invalidar_expresion()
            return ""
    
    def factor(self):
        preanalisis = self.get_preanalisis()
        if preanalisis == '(':
            self.coincidir('(')
            posicion = self.expr()
            self.coincidir(')')
            return posicion
        elif preanalisis.isdigit():
            numero = self.numero()
            posicion = self.gda.insertar_nodo("num",numero," ")
            return posicion
        else:
            pos_identificador = self.identificador()
            posicion = self.gda.insertar_nodo("id",pos_identificador," ")
            return posicion

    def resto_term(self,posicion1):
        preanalisis = self.get_preanalisis()
        if preanalisis == '*':
            self.coincidir('*')
            posicion2 = self.factor()
            nueva_posicion = self.gda.insertar_nodo('*',posicion1,posicion2)
            return self.resto_term(nueva_posicion)
        elif preanalisis == '/':
            self.coincidir('/')
            posicion2 = self.factor()
            nueva_posicion = self.gda.insertar_nodo('/',posicion1,posicion2)
            return self.resto_term(nueva_posicion)
        else:
            return posicion1
    
    def term(self):
        posicion1 = self.factor()
        return self.resto_term(posicion1)
        
    def resto_expr(self,posicion1):
        preanalisis = self.get_preanalisis()
        if preanalisis == '+':
            self.coincidir('+')
            posicion2 = self.term()
            nueva_posicion = self.gda.insertar_nodo('+',posicion1,posicion2)
            return self.resto_expr(nueva_posicion)
        elif preanalisis == '-':
            self.coincidir('-')
            posicion2 = self.term()
            nueva_posicion = self.gda.insertar_nodo('-',posicion1,posicion2)
            return self.resto_expr(nueva_posicion)
        else:
            return posicion1
    
    def expr(self):
        posicion1 = self.term()
        return self.resto_expr(posicion1)
    
    #Inicializar
    def comprobar_final_cadena(self) -> bool:
        if self.get_preanalisis() != ' ':
            self.invalidar_expresion()

    def iniciar_analisis(self):
        self.expr()
        self.comprobar_final_cadena()
        print(self.expresion, end='')
        if self.es_expresion_valida:
            print("-> Válido")
        else:
            print("-> No válido")
    
    def reiniciar_analizador(self):
        self.gda.limpiar_elementos()
        self.tabla_simbolos.limpiar_elementos()
        self.set_expresion('')
        self.reiniciar_posicion()
        self.validar_expresion()