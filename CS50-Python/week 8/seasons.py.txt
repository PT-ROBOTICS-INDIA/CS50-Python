import sys
import re
from datetime import date
import inflect

p = inflect.engine()

def main():
    birth_date = input("Date of Birth: ")
    try:
        if not re.search(r"^\d{4}-\d{2}-\d{2}$", birth_date):
            sys.exit("Invalid date")

        year, month, day = birth_date.split("-")
        minutes = calculate_minutes(int(year), int(month), int(day))

        msg = p.number_to_words(minutes, andword="")
        msg = msg.replace("  ", " ").capitalize()
        print(f"{msg} minutes")

    except ValueError:
        sys.exit("Invalid date")

def calculate_minutes(y, m, d):
    dob = date(y, m, d)
    today = date.today()
    diff = today - dob
    return diff.days * 24 * 60

if __name__ == "__main__":
    main()
