# Diccionarios
def p(texto):
    l = 80 - len(texto)
    print("-" * l, texto)


#
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
#
p("Dictionary Items - Clave -Brand")
print(thisdict["brand"])
#
p("Dictionaries cannot have two items with the same key:")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)
#
p("Dictionary Length")
print(len(thisdict))
#
p("Dictionary Items anda Data type")
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(thisdict)
print(type(thisdict))
#
p("Accessing Items")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
print(x)
p("car.get('model')")
print(thisdict.get("model"))
p("Get Keys")
x = thisdict.keys()
print(x)
#
###################################
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()
p("car.get('color')") 
car["color"] = "white"
print(car.get("color")) #after the change

p("Get Values")
p("The values() method will return a list of all the values in the dictionary.")
x = car.values()

car["year"] = 2020
p("after the change ")
print(x)
car["color"] = "red"
p("before the change")
print(x)

p("Get Items")
p("The items() method will return each item in a dictionary, as tuples in a list.")
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x)
car["year"] = 2020
print(x)  # after the change
#
p("ADD a new item: car['color']='red'")
car["color"] = "red"
print(x)  # after the change
p("Check if 'model' is present in the dictionary:")
if "model" in car:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

p("Change Values")
car["year"] = 2018
print(car)

p("Update Dictionary")
car.update({"year": 2020})
print(car)

car["color"] = "black"
car.update({"year": 2021})
print(car)

car.update({"color": "green"})
car.update({"year": 2022})
print(car)

# Python - Remove Dictionary Items
p("Removing Items")
thisdict.pop("model")
print(thisdict)

p("The popitem() method removes the last inserted item")
thisdict.popitem()
print(thisdict)

p("The del keyword removes the item with the specified key name:")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)

p("The clear() method empties the dictionary:")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)
p("The del keyword can also delete the dictionary completely:")
p("#this will cause an error because 'thisdict' no longer exists. ")
del thisdict
# print(thisdict)
