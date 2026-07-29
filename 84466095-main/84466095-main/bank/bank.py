new=input("Greeting: ").lower().strip()
if new.startswith("hello"):
    print("$0")
elif new.startswith("h"):
    print("$20")
else:
    print("$100")


