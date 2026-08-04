grocery_list={}
while True:
    try:
        grocery=input().strip().upper()
        if grocery in grocery_list:
            grocery_list[grocery]+=1
        else:
            grocery_list[grocery]=1
    except EOFError:
        break
for grocery in sorted(grocery_list.keys()):
    print(f"{grocery_list[grocery]} {grocery.upper()}")

