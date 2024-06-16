def calculator(operator, num1, num2):
    result = match operator:
        case '+':
            num1 + num2
        case '-':
            num1 - num2
        case '*':
            num1 * num2
        case '/':
            num1 / num2 if num2 != 0 else "Division by zero"
        case _:
            "Invalid operator"

    return result

# Example usage
print(calculator('+', 5, 3))  # Output: 8
print(calculator('-', 10, 4))  # Output: 6
print(calculator('*', 7, 2))  # Output: 14
print(calculator('/', 8, 0))  # Output: Division by zero
print(calculator('%', 4, 2))  # Output: Invalid operator

