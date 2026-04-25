def main() -> None:
    b_year: int = int(input("Enter your birth year: "))
    curr_year: int = 2025

    age: int = curr_year - b_year
    
    print(f"Your age is: {age}")


if __name__ == "__main__":
    main()