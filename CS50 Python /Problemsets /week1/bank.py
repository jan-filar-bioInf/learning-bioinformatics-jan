x = input("Greeting: ").strip().lower()

# response = not Hello get $100
# response = word starting with H get $20

if x .startswith("hello"):
    print("$0")
elif x .startswith("h"):
    print("$20")
else:
    print("$100")
