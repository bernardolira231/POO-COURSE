# class Person:
#     pass
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year

#     def description(self):
#         return '{} nacio en el {}'.format(self.name, self.year)

#     def comment(self, phrase):
#         return '{} dice {}'.format(self.name, phrase)

# doctor = Person('Jose', 2000)
# print(doctor.description())
# print(doctor.comment("Hola que tal"))

#Modificar un atributo

class Email:
    def __init__(self):
        self.send = False
    def send_email(self):
        self.send = True

mail = Email()

print(mail.send)
mail.send_email()
print(mail.send)
