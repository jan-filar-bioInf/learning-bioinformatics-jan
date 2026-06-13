#build a list of names

import inflect
p = inflect.engine()

names = []

#repeat asking the user for name
while True:
    try:
        name =input("Name: ")
#add input/name into list/names
        names.append(name)
#break while if ctrl + D
    except EOFError:
        print()
        break
#join the names from list / bring into a variable
jointnames = p.join(names)
print(f"Adieu, adieu, to {jointnames}")


