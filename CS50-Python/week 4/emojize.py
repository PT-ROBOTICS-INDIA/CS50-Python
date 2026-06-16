
import emoji

def main():

    user_input = input("Input: ")
    output = emoji.emojize(user_input,language='alias')

    print(output)

if __name__ == "__main__":
    main()
