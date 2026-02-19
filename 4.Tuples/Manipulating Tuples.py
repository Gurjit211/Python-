#Manipulating Tuples

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       # add item 
temp.pop(3)                 # remove item
temp[2] = "Finland"         # change item
countries = tuple(temp)
print(countries)


countries2 = ("Pakistan", "Afghanistan", "Bangladesh", "SriLanka")
countries3 = ("Vietnam", "India", "China")
southEastAsia = countries3 + countries2
print(southEastAsia)

