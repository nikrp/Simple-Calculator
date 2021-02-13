# This is my calculator

# Setting the total function.
total = 0

def greeting():
    print("\tHello, my name is Nikhil and this is my calculator! This calculator took")
    print("a while to make, but I finally did it with some help! I hope you like my")
    print("calculator!\n\n")

def instructions():
    print("\tMy calculator can do addition, subtraction, multiplication, division,")
    print("exponentiation, comparison, decimals, and a surprise category! My calculator")
    print("can't do multiple operation at the same time(e.g. 100 + 20 / 50 * 30 - 1).")
    print("My calculator can only do one operation at a time(e.g. 100 + 100 + 387).")
    print("More information below!\n\n")

def printVal(val):
    if val % int(val) == 0:
        val = int(val)
    else:
        val = round(val, 2)
    return str(val)

# Addition category
def addition():
    global total
    newTotal = ""
    print("Enter the numbers of your equation (e.g. 100 20 30): ", end="")
    myList = list(map(float, input().split()))
    for entry in myList:
        total = total + entry
        if len(newTotal) != 0:
            newTotal = newTotal + " + " + printVal(entry)
        else:
            newTotal = printVal(entry)
    total = f"{newTotal} = {printVal(total)}"

# Subtraction category
def subtraction():
    global total
    newTotal = ""
    print("Enter the nubers of your equation (e.g. 100 20 30): ", end="")
    myList = list(map(float, input().split()))
    for idx in range(0, len(myList)):
        if idx == 0:
            total = myList[idx]
        else:
            total = total - myList[idx]
        if len(newTotal) != 0:
            newTotal = newTotal + " - " + printVal(myList[idx])
        else:
            newTotal = printVal(myList[idx])
    total = f"{newTotal} = {printVal(total)}"

# Multiplication category
def multiplication():
    global total
    newTotal = ""
    print("Enter the nubers of your equation (e.g. 100 20 30): ", end="")
    myList = list(map(float, input().split()))
    for i in range(0, len(myList)):
        # If it is the first entry
        if i == 0:
            total = myList[i]
        else:
            total = total * myList[i]
        if len(newTotal) != 0:
            newTotal = newTotal + " * " + printVal(myList[i])
        else:
            newTotal = printVal(myList[i])
    total = f"{newTotal} = {printVal(total)}"



# Division category
def division():
    global total
    newTotal = ""
    isZeroDiv = False
    print("Enter the nubers of your equation (e.g. 100 20 30): ", end="")
    myList = list(map(float, input().split()))
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
            newTotal = newTotal + " / " + printVal(myList[i])
        else:
            newTotal = printVal(myList[i])
    if isZeroDiv == False:
        total = f"{newTotal} = {printVal(total)}"
    else:
        total = "Can't divide by 0!!"

# Exponentiation category
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

# Fibonacci numbers for surprise category
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
        print(f"  is a fibonacci number!")
    else:
        print(f"  is not a fibonacci number!")

# Surprise category        
def surprise():
    global total
    isPrime = True
    num = int(input("Pick a number: "))
    print(f"{num}:")
    # 1. Check for even or odd
    if num % 2 == 0:
        print(f"  is an even number!")
    else:
        print(f"  is an odd number!")
    
    # 2. Check if num is in the fibonacci numbers
    isFib(num)

    # 3. Check for prime or composite number
    for i in range(2, num-1):
        if num % i == 0:
            isPrime = False
            break
    if num < -1:
        total = f"  is composite!"
    elif num == 1 or num == 0 or num == -1:
        total = f"  is neither prime or composite!"
    elif isPrime == False:
        total = f"  is a composite number!"
    else:
        total = f"  is a prime number!"

# Compare category
def compare():
    global total
    print("\nAvalible comparisons:\n\t1. Greater Than\n\t2. Less Than\n\t3. Equal To\n\t4. Greater Than Or Equal To\n\t5. Less Than Or Equal To\n")
    compareOp = int(input("Pick the number that equals the comparison! 1, 2, 3, 4, or 5: "))
    n1 = int(input("Pick your first number: "))
    n2 = int(input("Pick your second number: "))
    if compareOp == 1:
        newTotal = n1 > n2
        total = f"{n1} > {n2} = {newTotal}"
    elif compareOp == 2:
        newTotal = n1 < n2
        total = f"{n1} < {n2} = {newTotal}"
    elif compareOp == 3:
        newTotal = f"{n1 == n2}"
        total = f"{n1} = {n2} = {newTotal}"
    elif compareOp == 4:
        newTotal = n1 >= n2
        total = f"{n1} >= {n2} = {newTotal}"
    elif compareOp == 5:
        newTotal = n1 <= n2
        total = f"{n1} <= {n2} = {newTotal}"

'''def decimal():
    global total
    newTotal = ""
    print("\nAvalible Operations:\n\t1. Addition\n\t2. Subtraction\n\t3. Multiplication\n\t4. Division\n")
    deciOper = int(input("Pick the number that equals the decimal operation! 1, 2, 3, or 4: "))
    print("\nEnter the numbers in your operation(e.g. 1.00 1.25 0.48): ", end="")
    myList = list(map(float, input().split()))
    print(myList)
    if deciOper == 1:
        for i in myList:
            total = total + i
        if len(newTotal) != 0:
            newTotal = newTotal + " + " + str(i)
        else:
            newTotal = str(i)
    total = f"{newTotal} = {total}"'''
        

# Goodbye function to print after operation is completed
def goodbye():
    print("\n\tI hoped you like my calculator! It took two days and lots of help to")
    print("make! I will probably make an improved calculator in the future!")
    print("THIS IS NIKHIL'S CALCULATOR!!!")

# Run function, what happens when code runs
def run():
    global total
    greeting()
    instructions()
    
    total = 0
    
    print("Pick an operation:\n\t1. Surprise!\n\t2. Addition\n\t3. Subtraction\n\t4. Multiplication\n\t5. Division\n\t6. Exponentiation\n\t7. Comparison\n")
    userOperation = input("Pick the number that equals the operation, 1, 2, 3, 4, 5, 6, or 7: ")
    if userOperation.lower() == "1":
        surprise()
    elif userOperation.lower() == "2":
        addition()
    elif userOperation.lower() == "3":
        subtraction()
    elif userOperation.lower() == "4":
        multiplication()
    elif userOperation.lower() == "5":
        division()
    elif userOperation.lower() == "6":
        exponents()
    elif userOperation.lower() == "7":
        compare()
    else:
        total = "Invalid operation, pick [1-7]!"

# Main function, what to run
if __name__ == "__main__":
    run()
    print(total)
    goodbye()
