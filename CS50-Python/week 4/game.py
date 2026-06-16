import random
import sys

def main():

    level = get_valid_level()

    target = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                continue
        except ValueError:
            continue

        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            sys.exit()

def get_valid_level():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                return n
        except ValueError:
            pass

if __name__ == "__main__":
    main()
