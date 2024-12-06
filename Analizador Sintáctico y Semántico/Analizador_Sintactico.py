FINAL_CADENA = ' '

class AnalizadorSintactico:
    def __init__(self):
        self.expresion = ''
        self.posicion_actual = 0
        self.es_expresion_valida = True
        self.resultado = ''

    def set_expresion(self, expresion:str):
        self.expresion = expresion + FINAL_CADENA

    def invalidar_expresion(self):
        self.es_expresion_valida = False

    def validar_expresion(self):
        self.es_expresion_valida = True

    def reiniciar_posicion(self):
        self.posicion_actual = 0
    
    def reiniciar_resultado(self):
        self.resultado = ''

    def get_preanalisis(self) -> str:
        return self.expresion[self.posicion_actual]

    def coincidir(self, caracter:str):
        if caracter ==  self.get_preanalisis():
            if(self.posicion_actual < len(self.expresion)-1):
                self.posicion_actual += 1
        else:
            self.invalidar_expresion()
    
    def digito(self):
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
        else:
            self.invalidar_expresion() 
        
        return preanalisis

    def factor(self):
        preanalisis = self.get_preanalisis()
        if preanalisis == '(':
            self.coincidir('(')
            expresion_t = self.expr()
            self.coincidir(')')
            return expresion_t
        else:
            digito_t = self.digito()
            return digito_t

    def resto_term(self,her):
        preanalisis = self.get_preanalisis()
        if preanalisis == '*':
            self.coincidir('*')
            factor_t = self.factor()
            resto_term_t = self.resto_term(her + factor_t + '*')
            return resto_term_t
        elif preanalisis == '/':
            self.coincidir('/')
            factor_t = self.factor()
            resto_term_t = self.resto_term(her + factor_t + '/')
            return resto_term_t
        else:
            return her
    
    def term(self):
        factor_t = self.factor()
        return self.resto_term(factor_t)

    def resto_expr(self,her):
        preanalisis = self.get_preanalisis()
        if preanalisis == '+':
            self.coincidir('+')
            term_t = self.term()
            resto_expresion_t = self.resto_expr(her + term_t + '+')
            return resto_expresion_t
        elif preanalisis == '-':
            self.coincidir('-')
            term_t = self.term()
            resto_expresion_t = self.resto_expr(her + term_t + '-')
            return resto_expresion_t
        else:
            return her
    
    def expr(self):
        term_t = self.term()
        return self.resto_expr(term_t)

    def comprobar_final_cadena(self) -> bool:
        if self.get_preanalisis() != ' ':
            self.invalidar_expresion()

    def iniciar_analisis(self):
        self.resultado = self.expr()
        self.comprobar_final_cadena()
        print(self.expresion, end='')
        if self.es_expresion_valida:
            print("-> Válido")
        else:
            print("-> No válido")