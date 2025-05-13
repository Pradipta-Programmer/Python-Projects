print("Welcome to the Guess the Number Game!")
while True:
    import random
    random_number= random.randint(1, 100)
    print("Start guessing the number which is between 1 - 100\n")
    attempt= 0
    guess= 0
    while guess != random_number:
        try:
            guess = int(input("Your Guess: "))
            if guess < random_number:
                print("Wrong\n", "Your Guess is Lower than the Real Number")
                attempt+= 1
            elif guess > random_number:
                print("Wrong\n", "Your Guess is Higher than the Real Number")
                attempt+= 1
            else:
                print("Congratulations!!!! You Guessed the Number!!!!")
                print(f"You took {attempt} attempts to guess it")
        except ValueError:
            print("Please enter a valid number!")
        
    answer= input("Want to play again?! Y/N\n >>> ")
    answer= answer.upper()
    while True:
        match answer:
            case 'Y':
                break
            case 'N':
                print("Thank You for Playing 😊")
                exit()
            case _:
                print("Invalid input", "\n", "Try Again")
                answer= input(">>> ").upper()