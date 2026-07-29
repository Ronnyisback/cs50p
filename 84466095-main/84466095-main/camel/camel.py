camel=input("Input Camelcase:")
print("Snake_Case=", end="")
for c in camel:
   if c.isupper():
      print("_"+c.lower(), end="")
   elif c.islower():
      print(c,end="")

