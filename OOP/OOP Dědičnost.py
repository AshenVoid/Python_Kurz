class Animals:
    def __init__(self, weight, age):
        self.weight = weight
        self.age = age

    def look(self):
        print("I am looking")

    def breathe(self):
        print("I am breathing")

    def __repr__(self):
        return f"Animals(weight={self.weight}, age={self.age})"

class Fish(Animals):
    def swim(self):
        print("I am swimming")

    def __repr__(self):
        return f"Fish(weight={self.weight}, age={self.age})"

class Mammal(Animals):
    def run(self):
        print("I am running")

    def __repr__(self):
        return f"Mammal(weight={self.weight}, age={self.age})"

class Bird(Animals):
    def fly(self):
        print("I am flying")

    def __repr__(self):
        return f"Bird(weight={self.weight}, age={self.age})"

class DomesticDog(Mammal):
    def __init__(self, weight, age, breed, coat_color):
        super().__init__(weight, age)
        self.breed = breed
        self.coat_color = coat_color

    def bark(self):
        print("I am barking")

    def retrieve(self):
        print("I am retrieving")

    def __repr__(self):
        return f"DomesticDog(weight={self.weight}, age={self.age}, breed={self.breed}, coat_color={self.coat_color})"


cap = Bird(30, 2)
cap.fly()
print(cap)
cap.look()
