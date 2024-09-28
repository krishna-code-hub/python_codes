class Father():
    name = 'Robert'


class Person(Father):
    def __init__(self, name):
        self.fathername = self.name
        print(self.name)
        self.name = name


    def introduce(self):
        print("My name is", self.name, "son of", self.fathername, Father.name)


king = Person("Joffrey")
king.introduce()
