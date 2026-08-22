import inflect
p=inflect.engine()
names=[]
while True:
    try:
        usrinp=input("Name: ")
        if usrinp.strip():
            names.append(usrinp.strip())
    except EOFError:
        print()
        break
formanames=p.join(names)
print(f"Adieu, adieu, to {formanames}")
