class Person:

    def __init__(self , name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")

person = Person("Hasindu")

# print(person.name)
person.talk()

bob = Person("Oscar")
bob.talk()