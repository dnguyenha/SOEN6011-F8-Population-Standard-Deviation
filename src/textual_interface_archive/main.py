from standard_deviation import calculate_statistics


def get_revenue_values():
    """Read daily revenue values from the textual user interface."""

    user_input = input(
        "Enter daily rental revenues separated by spaces: "
    )

    values = []

    for item in user_input.split():
        values.append(float(item))

    return values


def main():
    """Run the textual user interface."""

    print("Population Standard Deviation Calculator")
    print("----------------------------------------")

    while True:

        try:
            revenues = get_revenue_values()

            if len(revenues) == 0:
                print("Error: At least one revenue value is required.\n")
                continue

            mean, standard_deviation = calculate_statistics(revenues)

            print("\nRevenue values:")
            print(" ".join(f"{value:.2f}" for value in revenues))

            print(f"\nNumber of revenue values: {len(revenues)}")
            print(f"Arithmetic mean: {mean:.2f}")
            print(f"Population standard deviation (σ): {standard_deviation:.2f}")

        except ValueError:
            print("\nError: Enter only numerical revenue values separated by spaces.")

        # Ask whether to perform another calculation
        while True:
            choice = input("\nPerform another calculation? (Y/N): ").strip().upper()

            if choice == "Y":
                print()
                break

            elif choice == "N":
                print("\nThank you for using the Population Standard Deviation Calculator.")
                return

            else:
                print("Please enter Y or N.")


if __name__ == "__main__":
    main()
