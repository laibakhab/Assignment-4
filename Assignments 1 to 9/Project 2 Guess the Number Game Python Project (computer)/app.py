import random

print("Wellcome to the guess the number game! ")
print("Think of a number between 1 to 100 , and i will ty to guess it. ")
print("You can tell me if my guess is too high (H) , too low (L) , or correct (C).")


low = 1
high = 100
guesses = 0

while True:
    guess = random.randint(low , high)
    guesses += 1

    print(f"My guess is : {guess}")
    user_input = input("Is my guess too high (H) , too low (L) , or correct (C) ?").upper()


    if user_input == "H":
        high = guess - 1
    elif user_input == "L":
        low = guess + 1
    elif user_input == "C":
        print(f"yay | I guessed your number is {guess} in {guesses} tries|")    
        break
    else:
        print("Invalid Input. Please enter H , L , C ")    