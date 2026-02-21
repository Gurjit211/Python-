# One child class inherits from one parent class.

class Parent:

    def show(self):   # 'self' refers to the current object (instance) calling this method
        print("This is parent class")


class Child(Parent):

    pass   # 'pass' is used to define an empty class (it does nothing but avoids an error)


obj = Child()
obj.show()
