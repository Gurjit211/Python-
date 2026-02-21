
# One child class inherits from more than one parent class.

class Father:
    def skill1(self):
        print("Driving")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    pass

obj = Child()
obj.skill1()
obj.skill2()
