x = 10
print(type(x))   

y = 3.14
print(type(y)) 
  
z = 2 + 3j
print(type(z))   

b = True
print(type(b))  


# Simple calculator in Python

num1 = float(input("Enter first number: "))
op = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == '+':
    print("Result:", num1 + num2)
elif op == '-':
    print("Result:", num1 - num2)
elif op == '*':
    print("Result:", num1 * num2)
elif op == '/':
    if num2 == 0:
        print("Cannot divide by zero!")
    else:
        print("Result:", num1 / num2)
else:
    print("Invalid operator")



