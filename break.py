import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

while True:
    guess = int(input("Guess the number between 1 and 10: "))
    
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Wrong guess. Try again!")
