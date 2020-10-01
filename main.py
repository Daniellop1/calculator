def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Simple calculator")
print("----------------------------")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("----------------------------")
while True:
    
    choice = input("Enter Operation ID: ")


    if choice in ('1', '2', '3', '4', 'Add', 'Subtract', 'Multiply', 'Divide'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == 'Add':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == 'Subtract':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == 'Multiply':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == 'Divide':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Incorrect operation ID")
