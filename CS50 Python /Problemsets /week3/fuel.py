def main():
    result = get_fuelload()
    print(f"{result}")

def get_fuelload():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)

            if x < 0 or y <=0 or x > y:
                continue


            result = round(x / y * 100)
            if result >=99:
                return "F"
            if result  <=1:
                return "E"
            else:
                return f"{result}%"

        except ValueError:
            continue
        except ZeroDivisionError:
            continue

main()






