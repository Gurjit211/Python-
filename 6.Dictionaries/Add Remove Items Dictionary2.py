#pop():
#The pop() method removes the key-value pair whose key matches the parameter passed.

info = {'name': 'Karan', 'age': 19, 'eligible': True}
info.pop('eligible')
print(info)
print("\n \n")
#popitem():
#The popitem() method removes the last inserted key-value pair from the dictionary.
info = {'name': 'Karan', 'age': 19, 'eligible': True, 'DOB': 2003}
info.popitem()
print(info)
print("\n \n")

#Apart from these three methods, we can also use the del keyword to remove a dictionary item.

info2 = {'name': 'Karan', 'age': 19, 'eligible': True, 'DOB': 2003}
del info2['age']
print(info2)
print("\n \n")

# If a key is not provided, the del keyword will delete the entire dictionary.

info3 = {'name': 'Karan', 'age': 19, 'eligible': True, 'DOB': 2003}
del info3
print(info3)
