# Write a Python program that asks the user to enter their name.;
# Then, display a welcome message in the following format using concatenation.


def main() -> None:
    name: str = str(input("Enter your name: "))
    print(f"Hello {name}, Welcome to NSBM!")


if __name__ == "__main__":
    main()
