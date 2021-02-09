# This is an improved version of my old calculator.

def greeting():
    print("    This is Nikhil, and I made this python calculator. It took some help, but I")
    print("managed to finish it in two days, I hope you like my calculator!!\n")

def instructions():
    print("    This calculator can only do addition, subtraction, multiplication,")
    print("and division.It can only do one operation at a time, so it can't do")
    print("num + num / num * num. It can do operations like num + num + num and")
    print("num * num * num.\n")

greeting()

instructions()

print("Permitted operations - addition, subtraction, division, and multiplication!\n")
userOperation = input("Which operation would you like to use?: ")
print("")
print("Enter the nubers of your equation (e.g. 100 20 30): ", end="")
myList = list(map(int, input().split()))

total = 0
if userOperation.lower() in "addition add +":
    for entry in myList:
        total = total + entry
    print(total)
elif userOperation.lower() in "subtraction subtract -":
    for entry in myList:
        if total == 0:
            total = entry
        else:
            total = total - entry
    print(total)
elif userOperation.lower() in "multiplication multiply * x":
    for entry in myList:
        if total == 0:
            total = entry
        else:
            total = total * entry
    print(total)
elif userOperation.lower() in "division divide /":
    for entry in myList:
        if total == 0:
            total = entry
        else:
            if entry == 0:
                print("Oops! Can't divide by zero!")
            else:
                total = total / entry
    print(total)

def goodbye():
    print("    I hoped you like my calculator! It took two days and lots of help to make!")
    print("I will probably make an improved calculator in the future which can do powers!")
    print("THIS IS NIKHIL'S CALCULATOR!!!")

goodbye()
