"""Custom exceptions for the population standard deviation application."""


class InvalidDayCountError(Exception):
    """Raised when the calculation period is invalid."""

class InvalidNumberError(Exception):
    """Raised when a revenue entry is not numerical."""

class NegativeValueError(Exception):
    """Raised when a revenue entry is negative."""