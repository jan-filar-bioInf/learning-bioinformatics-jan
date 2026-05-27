text = input("Input: ")
print("Output: ", end="")

#gehe jeden einzelnen letter in text durch
for c in text:
        # c ist in aeiou enthalten, gehe eins weiter
        if c.lower() in "aeiou":
            continue
        #gebe c aus
        print(c, end="")



print()

