def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date = input("Date: ").strip()

        # Check format 1: MM/DD/YYYY
        if "/" in date:
            try:
                m, d, y = date.split("/")
                m, d, y = int(m), int(d), int(y)
                if m > 12 or d > 31: continue
                print(f"{y:04}-{m:02}-{d:02}")
                break
            except ValueError: continue

        # Check format 2: Month DD, YYYY
        elif "," in date:
            try:
                # Remove comma and split
                month_day, year = date.split(",")
                month, day = month_day.split(" ")

                if month in months:
                    m = months.index(month) + 1
                    d = int(day)
                    y = int(year)
                    if d > 31: continue
                    print(f"{y:04}-{m:02}-{d:02}")
                    break
            except (ValueError, IndexError): continue

        else: continue

if __name__ == "__main__":
    main()
