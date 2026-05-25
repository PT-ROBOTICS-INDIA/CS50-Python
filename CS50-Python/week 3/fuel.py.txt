
def main():
    while True:
        fraction = input("Fraction: ")
        try:
            numerator, denominator = fraction.split("/")
            x = int(numerator)
            y = int(denominator)
            if x > y or y == 0 or x < 0 or y < 0:
                continue
            percentage = round((x / y) * 100)
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")

            break

        except (ValueError, ZeroDivisionError):
            pass

if __name__ == "__main__":
    main()
