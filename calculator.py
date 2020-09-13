def accept():
    num1 = int(input("Enter First number:"))
    num2 = int(input("\nEnter Second number:"))
    return num1,num2

def add():
    x,y = accept()
    return x+y

def sub():
    x, y = accept()
    return x - y

def mul():
    x, y = accept()
    return x * y

def div():
    x, y = accept()
    return x / y

def errorHandler():
    print("Invalid Option")
while True:
    print("Operations :\n"
          "1. Addition\n"
          "2. Substraction\n"
          "3. Multiplication\n"
          "4. Division\n"
          "5.Exit")
    choice = int(input("Enter Your Choice Of Operation:\n"))
    operations = {
        1: add,
        2: sub,
        3: mul,
        4: div,
        5: exit
    }
    output = operations.get(choice, errorHandler)()
    print(output)

