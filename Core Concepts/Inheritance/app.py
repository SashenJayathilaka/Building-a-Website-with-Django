class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def brake(self):
        print("Brake")

class Cat(Mammal):
    def be_annoying(self):
        print("Annoying")

dog1 = Dog()
dog1.walk()
dog1.brake()

cat = Cat()
cat.walk()
cat.be_annoying()