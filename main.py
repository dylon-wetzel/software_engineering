# Dylon Wetzel


def encode(password):
    encoded_password = ""
    for digit in password:
        new_digit = str(int(digit) + 3)
        encoded_password += new_digit
    return encoded_password

def decode(encoded_password):
    password = ""
    for digit in encoded_password:
        original_digit = str(int(digit) - 3)
        password += original_digit
    return password

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("\nPlease enter an option: ")
        if choice == "1":
            password = input("\nPlease enter your password to encode: ")
            encoded_password = encode(password)
            print("\nYour password has been encoded and stored!\n")
        elif choice == "2":
            # password = decode(encoded_password)
            print(f"\nThe encoded password is {encoded_password}, and the original password is {password}.\n".format(encoded_password, password))
        elif choice == "3":
            break


if __name__ == '__main__':
    main()

