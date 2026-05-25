
import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        if play_round(x, y):
            score += 1

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            n = int(input("level: "))
            if n in [1, 2, 3]:
                return n
        except valueerror:
            pass

def generate_integer(level):

    if level == 1:
        return random.randint(0, 9)

    elif level == 2:
        return random.randint(10, 99)

    elif level == 3:
        return random.randint(100, 999)

    else:
        raise value_error("Invalid Level")
def play_round(x, y):
    tries = 0
    while tries < 3:
        try:
            answer = int(input(f"{x} + {y} = "))

            if answer == x + y:
                return True
            else:
                print("EEE")
                tries += 1
        except ValueError:
            print("EEE")
            tries += 1

    print(f"{x} + {y} = {x + y}")

if __name__ == "__main__":
    main()
