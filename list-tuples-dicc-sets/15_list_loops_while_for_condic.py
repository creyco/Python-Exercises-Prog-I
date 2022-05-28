print("+" * 50, "Loops" )
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#  
print("+" * 50, "Loops Trought the index number" )
thislist = ["apple", "banana", "cherry"]
print(thislist)
for i in range(len(thislist)):
  print(thislist[i])
#
print("+" * 50, "While Loop" )
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#
print("+" * 50, "Looping Using List Comprehension" )
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#
print("+" * 50, "List Comprehension" )
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
#
for x in fruits:
  if "a" in x:  # print if exist letter  "a" in the element x
    newlist.append(x)
print(newlist)
#
print("+" * 50, "List Comprehension 2th method" )
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
#
print("!= 'apple' The condition is like a filter that only accepts the items that valuate to True")
newlist = [x for x in fruits if x != "apple"]  # condicionaL IF
print(newlist)
print("With no if statement")
newlist = [x for x in fruits]
print(newlist)
print("range(10)- The iterable can be any iterable object, like a list, tuple, set etc")
newlist = [x for x in range(10)]
print(newlist)
newlist = [x for x in range(10) if x < 5]
print(newlist)
#
print("The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list")
newlist = [x.upper() for x in fruits]
print(newlist)
print("Set all values in the new list to 'hello':")
newlist = ['hello' for x in fruits]
print(newlist)
#
print("Return 'orange' instead of 'banana':")
print(fruits)
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)