#Adding items to a dictionary:

#1. Create a new key and assign a value to it:
info = {'name': 'Karan', 'age': 19, 'eligible': True}
print(info)
info['DOB'] = 2001
print(info)
print("\n \n")
#2. Use the update() method:

info2 = {'name': 'Karan Sharma', 'age': 19, 'eligible': True}
print(info2)
info2.update({'age': 20})
info2.update({'DOB': 2001})
print(info2)
print("\n \n")
#3Removing items from dictionary:

info3 = {'name': 'Karan', 'age': 19, 'eligible': True}
info3.clear()
print(info3)
