def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Rule: 2 to 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Rule: First two must be letters
    if not s[0:2].isalpha():
        return False

    # Rule: No punctuation/spaces
    if not s.isalnum():
        return False

    # Rule: Numbers handling
    for i in range(len(s)):
        if s[i].isdigit():
            # First digit cannot be '0'
            if s[i] == '0':
                return False
            # Everything from this point to the end must be digits
            return s[i:].isdigit()

    # If no numbers were found, it's valid
    return True

if __name__ == "__main__":
    main()
