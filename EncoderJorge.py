class PasswordEncoder:

    def encode(self, password):
        encoded_password = ''.join(str((int(digit) + 3) % 10) for digit in password)
        return encoded_password

    def decode(self, encoded_password):
        decoded_password = []
        for j in encoded_password:
            i = int(j)
            i -= 3
            decoded_password.append(i)
        return decoded_password


def main():
    password_encoder = PasswordEncoder()

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("Please enter an option: ")

        if option == '1':
            password = input("Please enter your password to encode: ")
            encoded_password = password_encoder.encode(password)
            print(f"Your password has been encoded and stored!")

        elif option == '2':
            decoded_password = ''.join(map(str, password_encoder.decode(encoded_password)))
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")

        elif option == '3':
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.\n")

if __name__ == "__main__":
    main()

