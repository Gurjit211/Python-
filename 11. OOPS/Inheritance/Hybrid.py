#Combination of more than one type of inheritance.

class Grandparent:
    def show_grandparent(self):
        print("I am Grandparent")

class Parent1(Grandparent):
    def show_parent1(self):
        print("I am Parent1")

class Parent2(Grandparent):
    def show_parent2(self):
        print("I am Parent2")

class Child(Parent1, Parent2):
    def show_child(self):
        print("I am Child")

# Create object
obj = Child()

# Calling methods
obj.show_grandparent()
obj.show_parent1()
obj.show_parent2()
obj.show_child()

"""

🔹 What’s Happening Here?

Parent1 and Parent2 both inherit from Grandparent → Hierarchical

Child inherits from Parent1 and Parent2 → Multiple

Overall combination → Hybrid Inheritance


"""
