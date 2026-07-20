"""Custom exceptions for the population standard deviation application."""


class EmptyInputError(Exception):
    """Raised when the user provides no input."""

class InvalidNumberError(Exception):
    """Raised when the user enters a non-numerical value."""

class NegativeValueError(Exception):
    """Raised when the user enters a negative revenue value."""