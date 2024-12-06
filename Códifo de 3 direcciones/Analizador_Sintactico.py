from Tripletas import Tripletas
from Tabla_Simbolos import TablaSimbolos

FINAL_CADENA = ' '

class AnalizadorSintactico:
    def __init__(self):
        self.expresion = ''
        self.posicion_actual = 0
        self.es_expresion_valida = True
        self.tabla_simbolos = TablaSimbolos()
        self.tripletas = Tripletas()

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
            return numero
        else:
            identificador = self.identificador()
            return identificador

    def resto_term(self,argumento1):
        preanalisis = self.get_preanalisis()
        if preanalisis == '*':
            self.coincidir('*')
            argumento2 = self.factor()
            nuevo_argumento = self.tripletas.insertar_triplete('*',argumento1,argumento2)
            return self.resto_term(nuevo_argumento)
        elif preanalisis == '/':
            self.coincidir('/')
            argumento2 = self.factor()
            nuevo_argumento = self.tripletas.insertar_triplete('/',argumento1,argumento2)
            return self.resto_term(nuevo_argumento)
        else:
            return argumento1
    
    def term(self):
        argumento1 = self.factor()
        return self.resto_term(argumento1)
        
    def resto_expr(self,argumento1):
        preanalisis = self.get_preanalisis()
        if preanalisis == '+':
            self.coincidir('+')
            argumento2 = self.term()
            nuevo_argumento = self.tripletas.insertar_triplete('+',argumento1,argumento2)
            return self.resto_expr(nuevo_argumento)
        elif preanalisis == '-':
            self.coincidir('-')
            argumento2 = self.term()
            nuevo_argumento = self.tripletas.insertar_triplete('-',argumento1,argumento2)
            return self.resto_expr(nuevo_argumento)
        else:
            return argumento1
    
    def expr(self):
        argumento1 = self.term()
        return self.resto_expr(argumento1)
    
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
        self.tripletas.limpiar_elementos()
        self.tabla_simbolos.limpiar_elementos()
        self.set_expresion('')
        self.reiniciar_posicion()
        self.validar_expresion()