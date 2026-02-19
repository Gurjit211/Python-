colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#                  [0]      [1]           [2]           [3]            [4]

colors2 = ["Red", "Green", "Blue", "Yellow", "Green"]
#                    [-5]        [-4]         [-3]         [-2]           [-1]
print(colors2[-1])
print(colors2[-3])
print(colors2[-5])


# We can check if a given item is present in the list. This is done using the in keyword

colors3 = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors3:
    print("Yellow is present.")
else:
    print("Yellow is absent.")


    animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])  # using positive indexes
print(animals[-7:-2])  # using negative indexes

print(animals[4:])  # using positive indexes
print(animals[-4:])  # using negative indexes

print(animals[:6])  # using positive indexes
print(animals[:-3])  # using negative indexes


print(animals[::2])  # using positive indexes
print(animals[-8:-1:2])  # using negative indexes













