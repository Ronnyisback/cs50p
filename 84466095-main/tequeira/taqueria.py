food_list={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
food_cost=0.00
while True:
    try:
        food_input=input("What food do you want?").title().strip()
        if food_input in food_list:
            food_cost+=food_list[food_input]
            print(f"${food_cost:.2f}")
        else:
            print("Item: ")
    except EOFError:
        break



