import random

def main():
    score=0
    level=get_level()
    for _ in range(10):
        X=generate_integer(level)
        Y=generate_integer(level)
        tries=0
        while tries<3:
            try:
                answer=int(input(f"{X} + {Y} = "))
                if answer == X + Y:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries+=1
            except ValueError:
                print("EEE")
                tries+=1
        if tries == 3:
            print(f"{X} + {Y} = {X+Y}")

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level=int(input("Level: "))
            if level in [1,2,3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level==1:
        return random.randint(0,9)
    elif level==2:
        return random.randint(10,99)
    elif level==3:
        return random.randint(100,999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()
