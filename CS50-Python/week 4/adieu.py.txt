
import inflect
import sys

def main():
    p = inflect.engine()
    names = []

    while True:
        try:

            name = input("Name: ")
            names.append(name)
        except EOFError:

            print()
            break

    if names:
        formatted_names = p.join(names)
        print(f"Adieu, adieu, to {formatted_names}")

if __name__ == "__main__":
    main()
