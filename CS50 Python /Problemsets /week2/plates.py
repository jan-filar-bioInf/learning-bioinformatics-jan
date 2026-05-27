def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("valid")
    else:
        print("invalid")

def is_valid(s):
    #lenght of string between 2 and 6 characters
        if len(s) < 2 or len(s) > 6:
             return False

        #first two characters from alphabet
        if not s[0:2].isalpha():
             return False

        #only alphabet and numbers allowed
        if not s.isalnum():
             return False

        #numbers only allowed at the end , not middle
        for i in range(len(s)):
           if s[i].isdigit():
               #no 0 allowed as first number
               if s[i] == "0":
                    return False

               if not s[i:].isdigit():
                         return False
               return True

        return True

main()
