# Diccionarios
def p(texto):
    l = 80 - len(texto)
    print("-" * l, texto)

p("Loop Through a Dictionary")
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x) 

for x in thisdict:
  print(thisdict[x])

p("You can use the Values() and keys() method to return")
for x in thisdict.values():
  print(x) 
for x in thisdict.keys():
  print(x)

p("Key and Value")
for x, y in thisdict.items():
  print(x, y)   

p("Python - Copy Dictionaries")  
mydict = thisdict.copy()
print(mydict)

mydict = dict(thisdict)
print(mydict) 

p("Nested Dictionaries - Anidados")
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

p("Create three dictionaries, then create one dictionary that will contain the other three dictionaries:")
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
} 

print(myfamily)
