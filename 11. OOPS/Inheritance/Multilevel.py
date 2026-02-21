# A class inherits from a class, which also inherits from another class.

class Grandparent:
    def home(self):
        print("Owns house")

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

obj = Child()
obj.home()
