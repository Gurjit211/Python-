class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Create objects
a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()
