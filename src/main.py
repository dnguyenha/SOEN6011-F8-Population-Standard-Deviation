from exceptions import (
    EmptyInputError,
    InvalidNumberError,
    NegativeValueError,
)
from standard_deviation import (
    calculate_mean,
    count_values,
    population_standard_deviation,
)


def get_revenue_values():
    """
    Read and validate daily revenue values entered by the user.

    Returns:
        list[float]: Validated revenue values.

    Raises:
        EmptyInputError: If the user enters no values.
        InvalidNumberError: If any entered value is not numerical.
        NegativeValueError: If any entered value is negative.
    """

    user_input = input("Enter daily rental revenues separated by spaces: ")

    values = []

    for item in user_input.split():
        try:
            value = float(item)
        except ValueError as error:
            raise InvalidNumberError(f"'{item}' is not a valid numerical revenue value.") from error
        
        if value < 0:
            raise NegativeValueError(f"Revenue cannot be negative: {value:.2f}")
        
        values.append(value)

    return values

def display_results(revenues):
    """
    Calculate and display the population statistics.

    Args:
        revenues (list[float]): Validated daily revenue values.
    """

    mean = calculate_mean(revenues)
    standard_deviation = population_standard_deviation(revenues)

    print(f"\nNumber of revenue values: {count_values(revenues)}")
    print(f"Arithmetic mean: {mean:.2f}")
    print(f"Population standard deviation (σ): {standard_deviation:.2f}")


def ask_to_continue():
    """
    Ask whether the user wants to perform another calculation.

    Returns:
        bool: True to continue, or False to exit.
    """
    while True:
        choice = input("\nPerform another calculation? (Y/N): ").strip().upper()

        if choice == "Y":
            print()
            return True

        if choice == "N":
            return False

        print("Error: Please enter Y or N.")

def main():
    print("Population Standard Deviation Calculator")
    print("----------------------------------------")

    while True:
        try:
            revenues = get_revenue_values()
            display_results(revenues)

        except EmptyInputError as error:
            print(f"\nError: {error}")

        except InvalidNumberError as error:
            print(f"\nError: {error}")

        except NegativeValueError as error:
            print(f"\nError: {error}")

        if not ask_to_continue():
            print(
                "\nThank you for using the Population "
                "Standard Deviation Calculator."
            )
            break

if __name__ == "__main__":
    main()
