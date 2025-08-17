import random

computer = random.randint(1, 9)
count = 0

while True:
    user = int(input("Enter a number between 1 and 9:\n"))
    count += 1
    print(f"computer chose {computer}")
    if user == computer:
        print("You win!")
        break
    else:
        print("You lose! Try again.")