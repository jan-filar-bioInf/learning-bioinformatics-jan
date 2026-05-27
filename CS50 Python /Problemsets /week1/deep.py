# ask user for answer
x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

# match answer to accepted responses (cases)
match x:
    case "42" | "forty-two" | "forty two":
        print("yes")
    case _:
        print("no")
