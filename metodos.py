class Maths:
    def plus(self):
        self.num1 = 2
        self.num2 = 3

s = Maths()

s.plus()
# print(s.num1 + s.num2)


class Clothing:
    def __init__(self):
        self.brand = 'willow'
        self.size = 'M'
        self.color = 'Rojo'

tshirt = Clothing()
# print(tshirt.size)

class Calculator:
    def __init__(self, n1, n2):
        self.addition = n1 + n2
        self.substraction = n1 - n2
        self.multiplication = n1 * n2
        self.division = n1 / n2

val1 = int(input('Valor 1: '))
val2 = int(input('Valor 2: '))

operation = Calculator(val1, val2)

print(operation.addition)
