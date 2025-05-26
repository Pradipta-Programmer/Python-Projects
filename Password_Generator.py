print("Welcome to my Password Generator")
import random
import string
while True:
    while True:
        try:
            length= int(input("Enter the length of your desired password:==>  "))
            break
        except ValueError:
            print("Please enter a valid number.")

    def choice(h):
        g= h.lower()
        if g in ["yes", "y"]:
            return True
        elif g in ["no", "n"]:
            return False
        else:
            print("Invalid Input\n Try Again")
            return None

    def priority():
        list=["UpperCase Letters","LowerCase Letters","Digits","Special Characters"]
        answers= []
        for option in list:
            while True:
                choosen= input("Do you want to include {}? (y/n)\n".format(option))
                f= choice(choosen)
                if f!= None:
                    answers.append(f)
                    break
        return answers
                    
    def generator():
        includors= priority()
        overall= ""
        pw= ""
        p= 0
        for option in includors:
            if option== True:
                if p== 0:
                    overall+= string.ascii_uppercase
                    p= p+1
                elif p== 1:
                    overall+= string.ascii_lowercase
                    p= p+1
                elif p== 2:
                    overall+= string.digits
                    p= p+1
                elif p== 3:
                    overall+= string.punctuation
            else:
                p+=1
        for _ in range(0, length):
            pw+= random.choice(overall)
        return pw

    password= generator()
    print(f"Here is your newly generated password---> {password}")

    while True:
        new= input("Want to make another password? (y/n)\n")
        new= new.lower()
        if new in ["yes", "y"]:
            break
        elif new in ["no", "n"]:
            print("Thank You for Using my Password Generator 😊")
            exit()
        else:
            print("Invalid Input\n Try Again")