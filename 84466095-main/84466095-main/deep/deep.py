answer=input("What is the answer to the Great Question of Life,the Universe, and Everything?").strip().lower()
match answer:
    case "forty two" | "forty-two" | "42":
      print("Yes")
    case _:
      print("No")



