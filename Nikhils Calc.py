# This is an improved version of my old calculator.

total = 0

def greeting():
    print("This is Nikhil, and I made this python calculator. It took some help, but I")
    print("managed to finish it in two days, I hope you like my calculator!!\n")

def instructions():
    print("This calculator can only do addition, subtraction, multiplication,")
    print("division, and exponentiation. It can only do one operation at a time,")
    print("so it can't do \"num + num / num * num\". It can do operations like ")
    print("num + num + num and num * num * num.\n")


def addition():
    global total
    newTotal = ""
    print("Enter the nubers of your equation (e.g. 100 20 30): ", end="")
    myList = list(map(int, input().split()))
    for entry in myList:
        total = total + entry
        if len(newTotal) != 0:
            newTotal = newTotal + " + " + str(entry)
        else:
            newTotal = str(entry)
    total = f"{newTotal} = {total}"

def subtraction():
    global total
    newTotal = ""
    print("Enter the nubers of your equation (e.g. 100 20 30): ", end="")
    myList = list(map(int, input().split()))
    for idx in range(0, len(myList)):
        if idx == 0:
            total = myList[idx]
        else:
            total = total - myList[idx]
        if len(newTotal) != 0:
            newTotal = newTotal + " - " + str(myList[idx])
        else:
            newTotal = str(myList[idx])
    total = f"{newTotal} = {total}"

def multiplication():
    global total
    newTotal = ""
    print("Enter the nubers of your equation (e.g. 100 20 30): ", end="")
    myList = list(map(int, input().split()))
    for i in range(0, len(myList)):
        # If it is the first entry
        if i == 0:
            total = myList[i]
        else:
            total = total * myList[i]
        if len(newTotal) != 0:
            newTotal = newTotal + " * " + str(myList[i])
        else:
            newTotal = str(myList[i])
    total = f"{newTotal} = {total}"

def division():
    global total
    newTotal = ""
    print("Enter the nubers of your equation (e.g. 100 20 30): ", end="")
    myList = list(map(int, input().split()))
    for i in range(0, len(myList)):
        if i == 0:
            total = myList[i]
        else:
            if myList[i] == 0:
                isZeroDiv = True
                break
            else:
                total = total / myList[i]
        if len(newTotal) != 0:
            newTotal = newTotal + " / " + str(myList[i])
        else:
            newTotal = str(myList[i])
    if isZeroDiv == False:
        total = f"{newTotal} = {total}"
    else:
        total = "Can't divide by 0!!"

def exponents():
    global total
    num = int(input("Enter the number: "))
    expo = int(input("Enter the exponent: "))
    total = f"{num} to the power of {expo} is {num ** expo}"
    '''
    for entry in range(0, expo):
        if total == 0:
            total = num
        else:
            total = total * num
    if expo == 0:
        total = 1
    '''

def isFib(num):
    n1 = 0
    n2 = 1
    isFibNum = False

    if num == 0 or num == 1:
        isFibNum = True

    # Check until we find a fib number >= num
    while True:
        temp = n1 + n2
        if num == temp:
            isFibNum = True
            break
        if num > temp:
            break
        n1 = n2
        n2 = temp
    if isFibNum == True:
        print(f"{num} is a fibonacci number!")
    else:
        print(f"{num} is not a fibonacci number!")
        
def surprise():
    global total
    isPrime = True
    num = int(input("Pick a number: "))
    if num % 2 == 0:
        print(f"{num} is an even number!")
    else:
        print(f"{num} is an odd number!")

    isFib(num)

    # 3. Check for prime or composite number
    for i in range(2, num-1):
        if num % i == 0:
            isPrime = False
            break
    if num < 0:
        total = f"Not checking {num} for prime or composite test!"
    elif num == 1 or num == 0:
        total = f"{num} is neither prime or composite!"
    elif isPrime == False:
        total = f"{num} is a composite number!"
    else:
        total = f"{num} is a prime number!"
            

def goodbye():
    print("\nI hoped you like my calculator! It took two days and lots of help to make!")
    print("I will probably make an improved calculator in the future!")
    print("THIS IS NIKHIL'S CALCULATOR!!!")

def run():
    global total
    greeting()
    instructions()
    
    total = 0
    
    print("Pick an operation:\n\t1. Addition\n\t2. Subtraction\n\t3. Division\n\t4. Multiplication\n\t5. Exponentiation\n\t6. Surprise!!")
    userOperation = input("Pick the number that equals the operation, 1, 2, 3, 4, 5, or 6: ")
    if userOperation.lower() == "1":
        addition()
    elif userOperation.lower() == "2":
        subtraction()
    elif userOperation.lower() == "3":
        division()
    elif userOperation.lower() == "4":
        multiplication()
    elif userOperation.lower() == "5":
        exponents()
    elif userOperation.lower() == "6":
        surprise()
    else:
        total = "Invalid operation, pick [1-6]!"

if __name__ == "__main__":
    run()
    print(total)
    goodbye()
