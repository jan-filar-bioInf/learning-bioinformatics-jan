# Interpret and calculate a simple arithmetic expression

x, y, z = input("Expression: ").split(" ")
x = int(x)
z = int(z)

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z
elif y == "**":
    result = x ** z

print(f"result: {result: .1f}")



