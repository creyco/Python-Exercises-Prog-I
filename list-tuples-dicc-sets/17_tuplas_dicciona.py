# Tuplas
def p(texto):
    l = 80 - len(texto)
    print("-" * l, texto)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#
p("Tuple Length")
#thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#
p("Create Tuple With One Item")
thistuple = ("apple",)
print(thistuple , end=" len=")
print(len(thistuple), end=" " )
print(type(thistuple))
#
p("NOT a tuple")
thistuple = ("apple")
print(type(thistuple)) 
p("YES a tuple")
thistuple = "apple",
print(type(thistuple)) 
#
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1 , end=" | ")
print(tuple2 , end=" | ")
print(tuple3)
#
p("A tuple can contain different data types:")
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
#
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#
p("The tuple() Constructor")
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
#
