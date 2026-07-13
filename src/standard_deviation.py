"""Population standard deviation calculator using the two-pass algorithm."""


def population_standard_deviation(values):
    """Calculate the population standard deviation of a list of numbers."""
    mean = sum(values) / len(values)

    squared_difference_sum = 0.0

    for value in values:
        difference = value - mean
        squared_difference_sum += difference ** 2

    variance = squared_difference_sum / len(values)
    standard_deviation = variance ** 0.5

    return standard_deviation
