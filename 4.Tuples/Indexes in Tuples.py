country = ("Spain", "Italy", "India", "England", "Germany")
#                         [0]      [1]           [2]        [3]                  [4]
print(country[1])
print(country[3])
print(country[0])


'''
Similar to positive indexing, negative indexing is also used to access items, but from the end of the tuple. The last item has index [-1], the second last item has index [-2],
the third last item has index [-3], and so on.
'''

country = ("Spain", "Italy", "India", "England", "Germany")
#                        [0]      [1]            [2]               [3]            [4]
print("\n")
print(country[-1])
print(country[-3])
print(country[-4])

print("\n")
country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")

# Rest Of Indexing study from code with harry page
