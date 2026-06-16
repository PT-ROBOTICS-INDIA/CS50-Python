import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input.jpg output.jpg")

    valid_extensions = (".jpg", ".jpeg", ".png")
    if not sys.argv[1].lower().endswith(valid_extensions):
        sys.exit("Invalid input")

    try:
        shirt = Image.open("shirt.png")
        with Image.open(sys.argv[1]) as muppet:
            muppet = ImageOps.fit(muppet, shirt.size)
            muppet.paste(shirt, shirt)
            muppet.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
