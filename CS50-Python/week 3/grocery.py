def main():
    items = {}

    while True:
        try:
            item = input().upper()
            if item in items:
                items[item] += 1
            else:
                items[item] = 1
        except EOFError:
            # Sort the keys and print
            for key in sorted(items.keys()):
                print(f"{items[key]} {key}")
            break

if __name__ == "__main__":
    main()
