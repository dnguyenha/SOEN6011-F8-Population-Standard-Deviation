"""Tkinter GUI for the population standard deviation calculator."""

import tkinter as tk
from tkinter import messagebox

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


class PopulationStandardDeviationGUI:
    """Graphical user interface for the calculator."""

    def __init__(self):
        """Create and configure the main window."""
        self.window = tk.Tk()
        self.window.title("Population Standard Deviation Calculator")
        self.window.geometry("620x430")
        self.window.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        """Create the interface components."""
        title_label = tk.Label(
            self.window,
            text="Population Standard Deviation Calculator",
            font=("Arial", 16, "bold"),
        )
        title_label.pack(pady=(20, 10))

        instruction_label = tk.Label(
            self.window,
            text=(
                "Enter daily rental revenues separated by spaces.\n"
                "Example: 100 120 80 110 90"
            ),
            font=("Arial", 10),
        )
        instruction_label.pack(pady=5)

        self.input_entry = tk.Entry(
            self.window,
            width=60,
            font=("Arial", 11),
        )
        self.input_entry.pack(pady=12)
        self.input_entry.focus()

        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=5)

        calculate_button = tk.Button(
            button_frame,
            text="Calculate",
            width=12,
            command=self.calculate,
        )
        calculate_button.grid(row=0, column=0, padx=5)

        clear_button = tk.Button(
            button_frame,
            text="Clear",
            width=12,
            command=self.clear,
        )
        clear_button.grid(row=0, column=1, padx=5)

        exit_button = tk.Button(
            button_frame,
            text="Exit",
            width=12,
            command=self.window.destroy,
        )
        exit_button.grid(row=0, column=2, padx=5)

        result_label = tk.Label(
            self.window,
            text="Results",
            font=("Arial", 12, "bold"),
        )
        result_label.pack(pady=(20, 5))

        self.result_text = tk.Text(
            self.window,
            width=68,
            height=10,
            font=("Courier New", 10),
            state="disabled",
        )
        self.result_text.pack(padx=20, pady=5)

    def parse_revenue_values(self):
        """
        Read and validate revenue values from the input field.

        Returns:
            list[float]: Validated revenue values.

        Raises:
            EmptyInputError: If no input is provided.
            InvalidNumberError: If an item is not numerical.
            NegativeValueError: If a value is negative.
        """
        user_input = self.input_entry.get().strip()

        if user_input == "":
            raise EmptyInputError("Enter at least one revenue value.")

        values = []

        for item in user_input.split():
            try:
                value = float(item)
            except ValueError as error:
                raise InvalidNumberError(f"'{item}' is not a valid numerical value.") from error

            if value < 0:
                raise NegativeValueError(f"Revenue cannot be negative: {value:.2f}")

            values.append(value)

        return values

    def calculate(self):
        """Calculate and display the population statistics."""
        try:
            revenues = self.parse_revenue_values()

            mean = calculate_mean(revenues)
            standard_deviation = (population_standard_deviation(revenues))

            formatted_values = " ".join(f"{value:.2f}" for value in revenues)

            result = (
                f"Revenue values:\n"
                f"{formatted_values}\n\n"
                f"Number of values: {count_values(revenues)}\n"
                f"Arithmetic mean: {mean:.2f}\n"
                f"Population standard deviation: "
                f"{standard_deviation:.2f}"
            )

            self.display_result(result)

        except (
            EmptyInputError,
            InvalidNumberError,
            NegativeValueError,
        ) as error:
            messagebox.showerror(
                "Input Error",
                str(error),
            )

    def display_result(self, result):
        """Display text in the result area."""
        self.result_text.config(state="normal")
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, result)
        self.result_text.config(state="disabled")

    def clear(self):
        """Clear the input and result fields."""
        self.input_entry.delete(0, tk.END)

        self.result_text.config(state="normal")
        self.result_text.delete("1.0", tk.END)
        self.result_text.config(state="disabled")

        self.input_entry.focus()

    def run(self):
        """Start the Tkinter event loop."""
        self.window.mainloop()