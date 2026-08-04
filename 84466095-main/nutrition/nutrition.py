
def nutrition_facts():
    fruits = {
    "Apple": 130,
    "Avocado": 50,
    "Kiwifruit": 90,
    "Sweet Cherries": 100,
    "Pear": 100}
    fruit=input("What fruit?:").title().strip()
    if fruit in fruits:
        print(f"Calories: {fruits[fruit]}")
nutrition_facts()









