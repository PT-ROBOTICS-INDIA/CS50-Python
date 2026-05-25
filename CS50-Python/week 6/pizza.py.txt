import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv"):
        sys.exit("Usage: python pizza.py filename.csv")

    table = []
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)
            print(tabulate(table, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
