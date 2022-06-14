class Calculadora:
    def __init__(self, number):
        self.n = number
        self.data = [0 for i in range(number)]

    def inputdata(self):
        self.data = [int(input('Ingresar el dato ' +str(i+1)+ ' = ')) for i in range(self.n)]

class Basic_op(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 2)

    def addition(self):
        a,b, = self.data
        s = a + b
        print('El resultado es ', s)
    def substraction(self):
        a,b, = self.data
        r = a - b
        print('El resultado es ', r)

class Root(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 1)
    def squre_root(self):
        import math
        a, = self.data
        print('El resultado es: ', math.sqrt(a))

example = Root()
print(example.inputdata())
print(example.squre_root())
