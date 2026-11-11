import secrets
import string


def generate_password(length=16):
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    groups = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        "!@#$%^&*()-_=+",
    ]

    characters = [secrets.choice(group) for group in groups]
    alphabet = "".join(groups)

    characters.extend(
        secrets.choice(alphabet)
        for _ in range(length - len(characters))
    )

    secrets.SystemRandom().shuffle(characters)

    return "".join(characters)


def main():
    print("PASSWORD GENERATOR")

    while True:
        user_input = input(
            "\nEnter password length (4-128), or q to quit: "
        ).strip()

        if user_input.lower() == "q":
            break

        try:
            length = int(user_input)

            if not 4 <= length <= 128:
                print("Choose a length between 4 and 128.")
                continue

            password = generate_password(length)
            print(f"Generated password: {password}")

        except ValueError:
            print("Please enter a whole number.")


if __name__ == "__main__":
    main()
