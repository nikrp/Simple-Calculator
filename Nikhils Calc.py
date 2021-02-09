# This is an improved version of my old calculator.

def greeting():
    print("This is Nikhil, and I made this python calculator. It took some help, but I")
    print("managed to finish it in two days, I hope you like my calculator!!\n")

def instructions():
    print("This calculator can only do addition, subtraction, multiplication,")
    print("division, and exponentiation. It can only do one operation at a time,")
    print("so it can't do \"num + num / num * num\". It can do operations like ")
    print("num + num + num and num * num * num.\n")

greeting()

instructions()

print("Permitted operations - addition, subtraction, division, multiplication, and exponentiation!\n")
userOperation = input("Which operation would you like to use?: ")

total = 0
if userOperation.lower() in "addition add +":
    print("Enter the nubers of your equation (e.g. 100 20 30): ", end="")
    myList = list(map(int, input().split()))
    for entry in myList:
        total = total + entry

elif userOperation.lower() in "subtraction subtract -":
    print("Enter the nubers of your equation (e.g. 100 20 30): ", end="")
    myList = list(map(int, input().split()))
    for entry in myList:
        if total == 0:
            total = entry
        else:
            total = total - entry

elif userOperation.lower() in "multiplication multiply * x":
    print("Enter the nubers of your equation (e.g. 100 20 30): ", end="")
    myList = list(map(int, input().split()))
    for entry in myList:
        if total == 0:
            total = entry
        else:
            total = total * entry

elif userOperation.lower() in "division divide /":
    print("Enter the nubers of your equation (e.g. 100 20 30): ", end="")
    myList = list(map(int, input().split()))
    for entry in myList:
        if total == 0:
            total = entry
        else:
            if entry == 0:
                print("Oops! Can't divide by zero!")
            else:
                total = total / entry

elif userOperation.lower() in "exponentiation exponents powers ^":
    num = int(input("Enter the number: "))
    expo = int(input("Enter the exponent: "))
    for entry in range(0, expo):
        if total == 0:
            total = num
        else:
            total = total * num
    if expo == 0:
        total = 1

print(total)
    
def goodbye():
    print("\nI hoped you like my calculator! It took two days and lots of help to make!")
    print("I will probably make an improved calculator in the future!")
    print("THIS IS NIKHIL'S CALCULATOR!!!")

goodbye()
