def main():

    camel_input = input("camelCase: ")

    print("snake_case:",convert_to_snake(camel_input))

def convert_to_snake(s):

    snake_case = ""
    capitalise_next = False

    for char in s:

        if char.isupper():
            snake_case += "_" + char.lower()
        elif capitalise_next:
            snake_case+=char.upper()
            capitalise_next = False

        else:
            snake_case += char
    return snake_case

if __name__ == "__main__":
    main()
