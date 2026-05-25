import sys

def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".py"):
        sys.exit("Usage: python lines.py filename.py")

    try:
        with open(sys.argv[1], "r") as file:
            count = 0
            for line in file:
                if line.strip() and not line.strip().startswith("#"):
                    count += 1
            print(count)
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
