print("Basic Calculator using Python")
print("--------------------------------")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\nResults:\n")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} x {b} = {a * b}")

if b != 0:
    print(f"Division: {a} / {b} = {a / b}")
else:
    print("Division: Cannot divide by zero")

print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponent: {a} ** {b} = {a ** b}")
