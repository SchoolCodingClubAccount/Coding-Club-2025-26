import random

def play_game():
    count = 0

    number = random.randint(1,101)

    while True:
        guess = int(input("Guess a number between 1-100! "))

        if guess > number:
            print("Lower!")
            count+=1
        elif guess < number:
            print("Higher!")
            count += 1
        else:
            count += 1
            break

    print(f"Well done, you guessed it in {count} tries!")

print("GUESS A NUMBER!\n")
play_game()