def p(texto):
    l = 80 - len(texto)
    print("-" * l, texto)


print("Python Collections (Arrays)")
p("List       is a collection which is ordered and changeable. Allows duplicate members.")
p("Tuple      is a collection which is ordered and unchangeable. Allows duplicate members.")
p("Set        is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.")
p("Dictionary is a collection which is ordered** and changeable. No duplicate members.")
