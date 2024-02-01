import random

def guess (x):
    random_number = random.randint(1,x)
    guess = 0
    
    while guess != random_number:
        guess =int(input(f"Guess a number betweem 1 and {x}:"))
        if guess < random_number:
            print("Sorry, guess again . too low. ")
        elif guess > random_number:
            print("sorry , guess again. too high")

    print("Yay , congrats , you have guessed the {random_number} correctly")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c' and low != high:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could also be high b/c low = high 
        feedback = input(f"Is {guess} to high (H) , too low(L) , or correct (C)??").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print("Yay! The compter guessed your number ,{guess}, correctly! ")


    computer_guess(1000)

