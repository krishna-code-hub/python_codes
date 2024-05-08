

class Enemy:
    type_of_enemy: str
    health: int = 10
    attack: int = 20

    def __init__(self,type_of_enemy,health,attack):
        self.type_of_enemy = type_of_enemy
        self.health = health
        self.attack = attack

    def talk(self):
        print("I'm able to talk now")

    def get_values(self):
        print(f"type_of_enemy = {self.type_of_enemy} \
              health = {self.health} \
              attack = {self.attack} ")