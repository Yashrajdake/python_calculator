import math

print("--- Advanced Math Utility Tool ---")
ptint("***")

last_result = None

while True:
    print("\nAvailable Modes:")
    print("1. Basic Operations (+, -, *, /, **)")
    print("2. Square Root (sqrt)")

    if last_result is not None:
       print(f"-> Current Ans: {last_result}")

    mode = input("Select mode (1 or 2) or type 'q' to quit: ")

    if mode.lower() == 'q':
        print("Goodbye!")
        break

    if mode == "1":
        try:
            prompt1 = "Enter first number (or 'ans'): " if last_result is not None else "Enter first number:"
            val1 = input(prompt1) 

            if val1.lower() == 'ans' and last_result is not None:
                num1 = last_result
            else:
                num1 = float(val1)

            operation = input("Enter operator( +, -, *, /, ** ): ")

            prompt2 ="Enter second number ( or 'ans'): " if last_result is not None else "Enter second number:"
            val2 = input(prompt2)

            if val2.lower() == 'ans' and last_result is not None:
                num2 = last_result
            else:
                num2 = float(val2)

        except ValueError:
            print("Error: Invalid input! Please enter valid numbers only.")
            print("-" * 25)
            continue

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
        elif operation == "**" :
            result = num1 ** num2
            print("Result:",result)
        else:
            print("Invalid operator!")
    elif mode == "2":
        try:
            prompt_sqrt = "Enter number for square root (or 'ans'): " if last_result is not None else "Enter number  for square root: "
            val = input(prompt_sqrt)

            if val.lower() == 'ans' and last_result is not None:
               num1 = last_result
            else:
                num1 = float(val)

        except ValueError:
            print("Error: Invalid input! Please enter a valid number.")
            print("-" * 25)
            continue

        if num1 >= 0:
            result = math.sqrt(num1)
            print("Result:", result)
            last_result = result
        else:
            print("Error: Cannot calculate square root of a negative number!")
    else:
        print("Error: Invalid mode selection!")

    print("-" * 25)
