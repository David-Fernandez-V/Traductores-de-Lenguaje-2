FINAL_CADENA = ' '

class AnalizadorSintactico:
    def __init__(self):
        self.expresion = ''
        self.posicion_actual = 0
        self.es_expresion_valida = True

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
    
    def factor(self):
        preanalisis = self.get_preanalisis()
        if preanalisis == '0':
            self.coincidir('0')
        elif preanalisis == '1':
            self.coincidir('1')
        elif preanalisis == '2':
            self.coincidir('2')
        elif preanalisis == '3':
            self.coincidir('3')
        elif preanalisis == '4':
            self.coincidir('4')
        elif preanalisis == '5':
            self.coincidir('5')
        elif preanalisis == '6':
            self.coincidir('6')
        elif preanalisis == '7':
            self.coincidir('7')
        elif preanalisis == '8':
            self.coincidir('8')
        elif preanalisis == '9':
            self.coincidir('9')
        elif preanalisis == '(':
            self.coincidir('(')
            self.expr()
            self.coincidir(')')
        else:
            self.invalidar_expresion()

    def resto_term(self):
        preanalisis = self.get_preanalisis()
        if preanalisis == '*':
            self.coincidir('*')
            self.factor()
            self.resto_term()
        elif preanalisis == '/':
            self.coincidir('/')
            self.factor()
            self.resto_term()
        else:
            pass
    
    def term(self):
        self.factor()
        self.resto_term()

    def resto_expr(self):
        preanalisis = self.get_preanalisis()
        if preanalisis == '+':
            self.coincidir('+')
            self.term()
            self.resto_expr()
        elif preanalisis == '-':
            self.coincidir('-')
            self.term()
            self.resto_expr()
        else:
            pass
    
    def expr(self):
        self.term()
        self.resto_expr()

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
    