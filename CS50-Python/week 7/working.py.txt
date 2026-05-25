import re
import sys

def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")

def convert(s):
    # This regex is stricter: it ensures minutes are always 2 digits if present
    # and requires the word " to " as the separator.
    if matches := re.search(r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$", s):
        parts = matches.groups()
        time1 = format_time(parts[0], parts[1], parts[2])
        time2 = format_time(parts[3], parts[4], parts[5])
        return f"{time1} to {time2}"
    else:
        # If it uses a dash or has single-digit minutes like :7, it hits this
        raise ValueError

def format_time(hour, minute, am_pm):
    h = int(hour)
    # Validate hours and minutes
    if h > 12 or h < 1:
        raise ValueError
    if minute and int(minute) >= 60:
        raise ValueError

    # 24-hour conversion logic
    if am_pm == "PM" and h != 12:
        h += 12
    elif am_pm == "AM" and h == 12:
        h = 0

    m = minute if minute else "00"
    return f"{h:02}:{m}"

if __name__ == "__main__":
    main()
    
