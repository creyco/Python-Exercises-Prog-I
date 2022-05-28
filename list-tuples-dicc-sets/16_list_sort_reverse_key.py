def p(texto):
    l = 80 - len(texto)
    print("-" * l, texto)


p( "Python - Sort Lists")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(thislist)
thislist.sort()
print(thislist)
#
p( "Sort the list numerically:")
thislist = [100, 50, 65, 82, 23]
print(thislist)
thislist.sort()
print(thislist)
p( "Sort the list descending:")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#
p( "Sort the list descending:")
thislist = [100, 50, 65, 82, 23]
print(thislist)
thislist.sort(reverse = True)
print(thislist)
#
p("Customize Sort Function")
def myfunc(n):
    print (n -50)
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
print(thislist)
thislist.sort(key = myfunc)
print(thislist)

p("Case Insensitive Sort")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
print(thislist)
thislist.sort()
print(thislist)
p("Luckily we can use built-in functions as key functions when sorting a list.")
p("So if you want a case-insensitive sort function,") 
p("use str.lower as a key function:")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#
p("Reverse Order")
p("What if you want to reverse the order of a list, regardless of the alphabet?")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
