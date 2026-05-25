from validator_collection import validators

def main():
    email = input("What's your email address? ")
    try:
        # If this line succeeds, the email is valid
        validators.email(email)
        print("Valid")
    except:
        # If validators.email raises an error, we catch it here
        print("Invalid")

if __name__ == "__main__":
    main()
