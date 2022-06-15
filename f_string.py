# nombre = 'victor'
# edad = '25'

# print(f'Hola soy {nombre} y mi edad es {edad} años.')


class Estudiante:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __repr__(self):
        return f'{self.nombre} {self.apellido} {self.edad}'

newstudent = Estudiante('Victor', 'Cruz', 17)
print(f"{newstudent !r}")
