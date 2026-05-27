def main():
    meow(get_number())


def get_number():
    while True:
        number = int(input("What´s number? "))
        if number > 0:
             break
    return number

def meow(number):
    for _ in range(number):
        print("meow")
main()

