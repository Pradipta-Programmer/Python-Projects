# Copyright (c) 2025 Pradipta Singha
# This code is licensed under the MIT License.
print("Welcome to my Simple Calculator")
while(True):
    print("\n", "Enter: ", "\n", "1 for Addition", "\n", "2 for Subtraction",
          "\n", "3 for Multiplication", "\n", "4 for Division", "\n", 
          "5 if you are done","\n")
    a= int(input(">>>  "))
    match a:
        case 1:
            b= int(input("How many numbers you want to input: "))
            print("Enter the numbers: ")
            l= []
            for i in range(0, b):
                l.append(int(input()))
            s= sum(l)
            print("Addition of inputed numbers: ", s)
        case 2:
            print("Enter the first number from which 2nd number is subtracted: ")
            l= []
            for i in range(0, 2):
                l.append(int(input()))
            s= l[0]-l[1]
            print("Subtraction of inputed numbers: ", s)
        case 3:
            b= int(input("How many numbers you want to input: "))
            print("Enter the numbers: ")
            l= []
            s= 1
            for i in range(0, b):
                l.append(int(input()))
                s= s*l[i]
            print("Multiplication of inputed numbers: ", s)
        case 4:
            print("Enter the diviend, followed by divisor: ")
            l= []
            for i in range(0, 2):
                l.append(int(input()))
            s= l[0]/l[1]
            print("Division of inputed numbers: ", s)
        case 5:
            break
        case _:
            print("Invalid input", "\n", "Try Again")

print("Thank you for using my Simple Calculator 😊")