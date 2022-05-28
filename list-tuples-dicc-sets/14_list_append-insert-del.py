print("+" * 50 , "append" )
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
print("+" * 50, "Insert" )
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
print("+" * 50, "Extent" )
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
print("+" * 50, "Remove" )
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
print("+" * 50, "Pop(1)" )
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
print("+" * 50, "Pop() last" )
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
print("+" * 50, "Del lista[0]" )
thislist = ["apple", "banana", "cherry"]
print(thislist)
del thislist[0]
print(thislist)
print("+" * 50, "Del lista - borra la lista" )
thislist = ["apple", "banana", "cherry"]
print(thislist)
del thislist
## print(thislist) ---> da error -- NameError: name 'thislist' is not defined
print("+" * 50, "clear() Clear lista" )
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)