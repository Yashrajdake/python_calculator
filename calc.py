

print(  "---Simple Python Calculator---")

num1 = float(input("Enter first number: "))
operation = input("Enter operator( +, -, *, / ): ")
num2 = float(input("Enter second number: "))

if operation == "+":
    result = num1 + num2
    print("Result:", result)
elif operation == "-":
    result = num1 - num2
    print("Result:", result)
elif operation == "*" :
    result = num1 * num2
    print("Result:", result)
elif operation == "/" :
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error:Cannot divide by zero!")
else:
    print("Invalid operator!")
