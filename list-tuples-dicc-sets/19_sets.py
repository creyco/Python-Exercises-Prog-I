def p(texto):
    l = 80 - len(texto)
    print("-" * l, texto)

p("Create a Set:")
thisset = {"apple", "banana", "cherry"}
print(thisset)

p("Get the number of items in a set:")
print(len(thisset)) 

p("String, int and boolean data types:")
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False} 
print(set1, end=" ")
print(set2, end=" ")
print(set3)

p("A set can contain different data types:")
set1 = {"abc", 34, True, 40, "male"}
print(set1)

p("type()")
p("From Python's perspective, sets are defined as objects with the data type 'set'")
print(type(set1))

p("The set() Constructor")
p("Using the set() constructor to make a set:")
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) 

p("Access Items")
p("You cannot access items in a set by referring to an index or a key.")
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x) 

p("Check if 'banana' is present in the set:") 
print("banana" in thisset) 

p("Python - Add Set Items")
thisset.add("orange")
print(thisset)

p("Add Sets")
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

p("Add Any Iterable")
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset) 

p("Remove Item")
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) 

p("Remove 'banana' by using the discard() method:")
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset) 

p("Remove the last item by using the pop() method:")
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset) 

p("The clear() method empties the set:")
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) 

p("The del keyword will delete the set completely:")
thisset = {"apple", "banana", "cherry"}
del thisset
p("print(thisset) NameError: name 'thisset' is not defined\n")

p("Loop through the set, and print the values:")
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x) 

p("Join Two Sets")  
p("The union() method returns a new --> set3=set1.union(set2)")
set1 = {"a", "b" , "c"} ; print(set1, end=" ") 
set2 = {1, 2, 3}  ; print(set1, end=" ") 
set3 = set1.union(set2)
print(set3) 

p("The update() method inserts the items in set2 into set1:")
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1) 

p("Keep the items that exist in both set x, and set y:")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x) 

p("The intersection() method will return a new set, that only contains the items")
p("that are present in both sets.")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z) 

p("Keep All, But NOT the Duplicates")
p("The symmetric_difference() method will return a new set, that contains")
p("only the elements that are NOT present in both sets.")
x = {"apple", "banana", "cherry"}    ; print(x , end=" | ")
y = {"google", "microsoft", "apple"} ; print(y)
x.symmetric_difference_update(y)
print(x) 

p("Return a set that contains all items from both sets, except items that are")
p("present in both: ")
x = {"apple", "banana", "cherry"}    ; print(x , end=" | ")
y = {"google", "microsoft", "apple"} ; print(y)
z = x.symmetric_difference(y)
print(z)