
# Multiple child classes inherit from the same parent class.

class Parent:
    def property(self):
        print("Family property")

class Child1(Parent):
    pass

class Child2(Parent):
    pass


obj1 = Child1()

obj2 = Child2()

obj1.property()

obj2.property()
