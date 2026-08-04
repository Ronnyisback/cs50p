while True:
    try:
        fuel_fraction=input("How much fuel")
        x, y=fuel_fraction.split("/")
        x=int(x)
        y=int(y)
        if x>y or (x*y)<0:
            raise ValueError
        fuel_point=round(x/y*100)
        break
    except (ZeroDivisionError, ValueError):
        pass
if fuel_point<=1:
        print("E")
elif fuel_point>=99:
        print("F")
else:
     print(f"{fuel_point}%")


