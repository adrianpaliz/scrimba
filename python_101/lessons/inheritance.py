class Person:
    def move(self):
        print('Moves 4 paces')
    def rest(self):
        print('Gains 4 health points')
#character_1 = Person()
#character_1.move()

class Doctor(Person):
    def heal(self):
        print('Heals 10 healt points')
#character_1 = Doctor()
#character_1.move()
#character_1.heal()

class Fighter(Person):
    def fight(self):
        print('Do 10 health points of damage')
    def move(self):
        print('Moves 6 paces')
#character_1 = Fighter()
#character_1.fight() 
#character_1.move()

class Wizard(Doctor, Fighter):
    def cast_spell(self):
        print('Turns invisible')
    def heal(self):
        print('Heals 15 healt points')
character_1 = Wizard()
character_1.move()

