while True:
    print("\nType 'quit' to exit.")

    num1 = input("Enter the first number: ")
    if num1.lower() == "quit":
        break
    num2 = input("Enter the second number: ")
    if num2.lower() == "quit":
        break

    try:
        num1, num2 = float(num1), float(num2)
    except ValueError:
        print("Error: Please enter a valid number.")
        continue

    operation = input("Choose operation (+, -, *, /): ")
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero."
    else:
        print("Invalid operation. Try again.")
        continue

    print(
        f"Result: {int(result) if isinstance(result, float) and result.is_integer() else result}"
    )
