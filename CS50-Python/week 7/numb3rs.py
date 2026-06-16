import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # This regex ensures we don't have leading zeros (like 01 or 007)
    # unless the number itself is just '0'.
    pattern = r"^([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"

    if re.search(pattern, ip):
        return True
    return False

if __name__ == "__main__":
    main()
