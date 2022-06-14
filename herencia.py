class Pokemon:
    pass
    def __init__(self,name, typep):
        self.name = name
        self.typep = typep

    def description(self):
        return '{} es pokemon de tipo {}'.format(self.name, self.typep)

class Pikachu(Pokemon):
    def attack(self,typeattack):
        return '{} tipo de ataque {}'.format(self.name, typeattack)

class Charmader(Pokemon):
    def attack(self,typeattack):
        return '{} tipo de ataque {}'.format(self.name, typeattack)

newpokemon = Pikachu('Boby', 'Electrico')
print(newpokemon.description())
print(newpokemon.attack('Impactrueno'))
