# # Project 01: Simple Calculator

# ## Description
# A simple calculator developed using Python to perform basic mathematical operations. Users can enter two numbers and select an opertor to calulate the result.

# ## Features
# - Addition (+)
# - Subtraction (-)
# - Multiplication (*)
# - Division (/)

# ## Technologies
# - Python
# - Jupyter Notebook
# - Visual Studio Code (VS Code)

# ## Author
# Sumit Laxman Atloori

# ===================================================================================================

# Project 01: Simple Calculator

print("=" * 40)
print("          SIMPLE CALCULATOR")
print("=" * 40)

# Takeing Input From Users

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
operator = input("Enter Operator (+, -, *, /): ")

# Performing Calculations

if operator == "+":
    result = num1 + num2
    print("Addition:", result)

elif operator == "-":
    result = num1 - num2
    print("Subtraction:", result)

elif operator == "*":
    result = num1 * num2
    print("Multiplication:", result)

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Division:", result)
    else:
        print("Error: Cannot divide by zero.")

else:
    print("Invalid operator!")