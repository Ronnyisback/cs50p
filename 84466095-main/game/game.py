from random import randint
while True:
    n=input("Level: ")
    if n.isdigit() and int(n)>0:
        n=int(n)
        break
    else:
        continue
answer=randint(1,n)
while True:
    guess=input("Guess: ")
    if guess.isdigit() and int(guess)>0:
        guess=int(guess)
    else:
        continue
    if guess == answer:
        print("Just right!")
        break
    elif guess < answer:
        print("Too small!")
    elif guess > answer:
        print("Too large!")


