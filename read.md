def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


print("TEMPERATURE CONVERTER")
print("---------------------")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose 1 or 2: ")

if choice == "1":
    temp = float(input("Enter temperature in Celsius: "))
    result = celsius_to_fahrenheit(temp)
    print(f"{temp}°C = {result:.2f}°F")

elif choice == "2":
    temp = float(input("Enter temperature in Fahrenheit: "))
    result = fahrenheit_to_celsius(temp)
    print(f"{temp}°F = {result:.2f}°C")

else:
    print("Invalid choice")