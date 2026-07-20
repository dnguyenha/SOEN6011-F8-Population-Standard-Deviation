"""Population standard deviation implementation."""


def count_values(values):
    """
    Count the number of values without using len().

    Args:
        values (list[float]): Numerical population values.

    Returns:
        int: Number of values.
    """
    count = 0

    for _ in values:
        count += 1

    return count


def calculate_sum(values):
    """
    Calculate the total without using sum().

    Args:
        values (list[float]): Numerical population values.

    Returns:
        float: Sum of all values.
    """
    total = 0.0

    for value in values:
        total += value

    return total


def calculate_mean(values):
    """
    Calculate the arithmetic mean from scratch.

    Args:
        values (list[float]): Numerical population values.

    Returns:
        float: Arithmetic mean.
    """
    number_of_values = count_values(values)

    if number_of_values == 0:
        raise ValueError("At least one numerical value is required.")

    total = calculate_sum(values)

    return total / number_of_values


def population_standard_deviation(values):
    """
    Calculate population standard deviation using the two-pass algorithm.

    Args:
        values (list[float]): Numerical population values.

    Returns:
        float: Population standard deviation.
    """
    number_of_values = count_values(values)

    if number_of_values == 0:
        raise ValueError("At least one numerical value is required.")

    mean = calculate_mean(values)
    squared_difference_sum = 0.0

    for value in values:
        difference = value - mean
        squared_difference_sum += difference ** 2

    variance = squared_difference_sum / number_of_values
    standard_deviation = variance ** 0.5

    return standard_deviation