import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    # \b matches word boundaries to ignore 'album' or 'yummy'
    return len(re.findall(r"\bum\b", s, re.IGNORECASE))

if __name__ == "__main__":
    main()
