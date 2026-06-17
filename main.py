import random

number = random.randint(1, 10)

for attempt in range(10):
    guessed_num = int(input("Try to guess the number:"))
    if guessed_num == number:
        print("You WIN")
        break
    print(f"Sorry, that is not the number, try again (attempt {attempt})")
