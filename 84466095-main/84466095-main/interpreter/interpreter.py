expression = input("Expression: ").strip(" ")
x_str, y, z_str = expression.split(" ")
x = float(x_str)
z = float(z_str)
match y:
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "*":
        print(x * z)
    case "/":
        if z == 0:
            print("Error: Division by zero")
        else:
            print(x / z)
    case _:
        print("Error: Invalid operator")

