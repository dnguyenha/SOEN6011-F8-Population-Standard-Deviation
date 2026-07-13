from standard_deviation import population_standard_deviation

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

    try:
        revenues = get_revenue_values()

        if len(revenues) == 0:
            print("Error: At least one revenue value is required.")
            return

        result = population_standard_deviation(revenues)

        print(f"\nNumber of revenue values: {len(revenues)}")
        print(f"Population standard deviation: {result:.2f}")

    except ValueError:
        print(
            "Error: Enter only numerical revenue values separated by spaces."
        )

if __name__ == "__main__":
    main()