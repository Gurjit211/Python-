#We can use the copy() method to copy the contents of one dictionary into another dictionary.

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
newDictionary = info.copy()
print(newDictionary)

#Or we can use the dict() function to make a new dictionary with the items of the original dictionary.

info1 = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
newDictionary1 = dict(info1)
print(newDictionary1)
