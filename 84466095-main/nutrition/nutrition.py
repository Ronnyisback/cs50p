
def nutrition_facts():
    fruits = {
    "Apple": 130,
    "Avocado": 50,
    "Banana": 110,
    "Cantaloupe": 50,
    "Grapefruit": 60,
    "Grapes": 90,
    "Honeydew melon": 50,
    "Kiwifruit": 90,
    "Lemon": 15,
    "Lime": 20}
    fruit=input("What fruit?:").title().strip()
    if fruit in fruits:
        print(f"Calories: {fruits[fruit]}")
nutrition_facts()









