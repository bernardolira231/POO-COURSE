class Person:
    age = 27
    name = 'Victor'
    nacionality = 'Brasil'

doctor = Person()

# print('El nombre es:',doctor.name)#Victor
# print('La edad es:', getattr(doctor, 'age'))#27
# print('El doctor tiene una edad?', hasattr(doctor, 'age'))#true
# print('El doctor tiene una edad?', hasattr(doctor, 'last_name'))#false
# print(doctor.name)#Victor
# setattr(doctor, 'name', 'Hector')
# print(doctor.name)#Hector
# delattr(Person, 'nacionality')
# print(doctor.nacionality)#error
