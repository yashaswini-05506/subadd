num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform multiplication
product = num1 * num2

# Perform division with zero check
if num2 != 0:
    quotient = num1 / num2
else:
    quotient = "Undefined (division by zero)"

# Output the results
print(f"\nResults:")
print(f"Multiplication: {num1} × {num2} = {product}")
print(f"Division: {num1} ÷ {num2} = {quotient}")
