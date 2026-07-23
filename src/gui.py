"""Tkinter GUI for selecting a date range and entering daily revenues."""

import tkinter as tk
from datetime import timedelta
from tkinter import messagebox
from tkcalendar import DateEntry
from exceptions import (
    InvalidDayCountError,
    InvalidNumberError,
    NegativeValueError,
)
from standard_deviation import (
    calculate_mean,
    calculate_sum,
    count_values,
    population_standard_deviation,
)


class PopulationStandardDeviationGUI:
    """Graphical interface for the population standard deviation calculator."""

    MINIMUM_DAYS = 1
    MAXIMUM_DAYS = 31

    def __init__(self):
        """Create and configure the main application window."""
        self.window = tk.Tk()
        self.window.title("Population Standard Deviation Calculator")
        self.window.geometry("800x820")
        self.window.minsize(760, 750)

        self.revenue_entries = []

        self.create_widgets()

    def create_widgets(self):
        """Create the main interface components."""
        title_label = tk.Label(
            self.window,
            text="Daily Rental Revenue Calculator",
            font=("Arial", 18, "bold"),
        )
        title_label.pack(pady=(20, 5))

        instruction_label = tk.Label(
            self.window,
            text=(
                "Select a start date and enter the number of days "
                "for the calculation."
            ),
            font=("Arial", 10),
        )
        instruction_label.pack(pady=(0, 15))

        ## Selection Frame
        selection_frame = tk.LabelFrame(
            self.window,
            text="Calculation Period",
            padx=15,
            pady=12,
        )
        selection_frame.pack(fill="x", padx=25, pady=5)

        start_date_label = tk.Label(
            selection_frame,
            text="Start date:",
            font=("Arial", 10),
        )
        start_date_label.grid(
            row=0,
            column=0,
            padx=8,
            pady=8,
            sticky="e",
        )

        self.start_date_entry = DateEntry(
            selection_frame,
            width=16,
            date_pattern="yyyy-mm-dd",
        )
        self.start_date_entry.grid(
            row=0,
            column=1,
            padx=8,
            pady=8,
            sticky="w",
        )

        number_of_days_label = tk.Label(
            selection_frame,
            text="Number of days:",
            font=("Arial", 10),
        )
        number_of_days_label.grid(
            row=0,
            column=2,
            padx=8,
            pady=8,
            sticky="e",
        )

        self.number_of_days_entry = tk.Entry(
            selection_frame,
            width=8,
            justify="center",
        )
        self.number_of_days_entry.grid(
            row=0,
            column=3,
            padx=8,
            pady=8,
            sticky="w",
        )
        self.number_of_days_entry.insert(0, "7")

        generate_button = tk.Button(
            selection_frame,
            text="Generate Days",
            width=15,
            command=self.generate_days,
        )
        generate_button.grid(
            row=0,
            column=4,
            padx=10,
            pady=8,
        )

        selection_frame.columnconfigure(4, weight=1)

        self.period_label = tk.Label(
            self.window,
            text="No calculation period generated.",
            font=("Arial", 10, "italic"),
        )
        self.period_label.pack(pady=(10, 5))

        revenue_container = tk.LabelFrame(
            self.window,
            text="Daily Revenue",
            padx=10,
            pady=10,
        )
        revenue_container.pack(fill="x", padx=25, pady=8)

        self.canvas = tk.Canvas(
            revenue_container,
            height=245,
            highlightthickness=0,
        )

        scrollbar = tk.Scrollbar(
            revenue_container,
            orient="vertical",
            command=self.canvas.yview,
        )

        self.revenue_frame = tk.Frame(self.canvas)

        self.revenue_frame.bind( "<Configure>", self.update_scroll_region)

        self.canvas_window = self.canvas.create_window(
            (0, 0),
            window=self.revenue_frame,
            anchor="nw",
        )

        self.canvas.bind("<Configure>", self.resize_revenue_frame)

        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)

        scrollbar.pack(side="right", fill="y")

        placeholder_label = tk.Label(
            self.revenue_frame,
            text=("Select a start date and number of days, then click Generate Days."),
            font=("Arial", 10),
        )
        placeholder_label.pack(pady=30)

        ## Primary Action Frame
        primary_action_frame = tk.Frame(self.window)
        primary_action_frame.pack(pady=(5, 10))

        calculate_button = tk.Button(
            primary_action_frame,
            text="Calculate",
            width=18,
            font=("Arial", 10, "bold"),
            command=self.calculate,
        )
        calculate_button.pack()

        ## Result Frame
        result_frame = tk.LabelFrame(
            self.window,
            text="Calculation Results",
            padx=20,
            pady=12,
        )
        result_frame.pack(fill="x", padx=25, pady=(0, 10))

        self.period_result = tk.StringVar(value="No calculation has been performed.")
        self.days_result = tk.StringVar(value="—")
        self.total_result = tk.StringVar(value="—")
        self.mean_result = tk.StringVar(value="—")
        self.standard_deviation_result = tk.StringVar(value="—")

        period_label = tk.Label(
            result_frame,
            textvariable=self.period_result,
            font=("Arial", 10, "italic"),
            anchor="w",
        )
        period_label.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="w",
            pady=(0, 10),
        )

        result_labels = [
            ("Number of days:", self.days_result),
            ("Total revenue:", self.total_result),
            ("Average daily revenue:", self.mean_result),
            ("Population standard deviation:", self.standard_deviation_result,),
        ]

        for row_number, (label_text, result_variable) in enumerate(
            result_labels,
            start=1,
        ):
            description_label = tk.Label(
                result_frame,
                text=label_text,
                font=("Arial", 10),
                anchor="w",
            )
            description_label.grid(
                row=row_number,
                column=0,
                padx=(0, 25),
                pady=3,
                sticky="w",
            )

            value_label = tk.Label(
                result_frame,
                textvariable=result_variable,
                font=("Arial", 10, "bold"),
                anchor="e",
            )
            value_label.grid(
                row=row_number,
                column=1,
                pady=3,
                sticky="e",
            )

        result_frame.columnconfigure(0, weight=1)
        result_frame.columnconfigure(1, weight=1)

        ## Secondary Action Frame
        secondary_action_frame = tk.Frame(self.window)
        secondary_action_frame.pack(pady=(0, 15))

        clear_revenue_button = tk.Button(
            secondary_action_frame,
            text="Clear Revenue",
            width=14,
            command=self.clear_revenue_values,
        )
        clear_revenue_button.grid(row=0, column=0, padx=5)

        reset_button = tk.Button(
            secondary_action_frame,
            text="Reset",
            width=14,
            command=self.clear_generated_days,
        )
        reset_button.grid(row=0, column=1, padx=5)

        exit_button = tk.Button(
            secondary_action_frame,
            text="Exit",
            width=14,
            command=self.window.destroy,
        )
        exit_button.grid(row=0, column=2, padx=5)

    def get_number_of_days(self):
        """
        Read and validate the requested number of days.

        Returns:
            int: A valid number of days from 1 to 31.

        Raises:
            InvalidDayCountError: If the value is missing or invalid.
        """
        user_input = self.number_of_days_entry.get().strip()

        if user_input == "":
            raise InvalidDayCountError("Enter the number of days for the calculation.")

        try:
            number_of_days = int(user_input)
        except ValueError as error:
            raise InvalidDayCountError(
                "The number of days must be a whole number between 1 and 31."
            ) from error

        if (number_of_days < self.MINIMUM_DAYS or number_of_days > self.MAXIMUM_DAYS):
            raise InvalidDayCountError("The number of days must be between 1 and 31.")

        return number_of_days

    def get_revenue_values(self):
        """
        Read and validate generated daily revenue fields.

        Blank fields are interpreted as zero.

        Returns:
            list[float]: Revenue values for all generated dates.

        Raises:
            InvalidDayCountError: If no dates have been generated.
            InvalidNumberError: If an entered value is not numerical.
            NegativeValueError: If an entered value is negative.
        """
        if count_values(self.revenue_entries) == 0:
            raise InvalidDayCountError(
                "Generate the calculation period before calculating."
            )

        revenues = []

        for revenue_item in self.revenue_entries:
            current_date = revenue_item["date"]
            entry = revenue_item["entry"]
            user_input = entry.get().strip()

            if user_input == "":
                revenue = 0.0
            else:
                try:
                    revenue = float(user_input)
                except ValueError as error:
                    raise InvalidNumberError(
                        f"Revenue for "
                        f"{current_date.strftime('%A, %B %d, %Y')} "
                        f"must be a number or left blank."
                    ) from error

            if revenue < 0:
                raise NegativeValueError(
                    f"Revenue for "
                    f"{current_date.strftime('%A, %B %d, %Y')} "
                    f"cannot be negative."
                )

            revenues.append(revenue)

        return revenues

    def generate_days(self):
        """Generate one revenue field for each date in the selected period."""
        try:
            number_of_days = self.get_number_of_days()
        except InvalidDayCountError as error:
            messagebox.showerror("Invalid Calculation Period", str(error))
            return

        self.clear_revenue_frame()
        self.clear_results()

        start_date = self.start_date_entry.get_date()
        end_date = start_date + timedelta(days=number_of_days - 1)

        header_date_label = tk.Label(
            self.revenue_frame,
            text="Date",
            font=("Arial", 10, "bold"),
            width=30,
            anchor="w",
        )
        header_date_label.grid(
            row=0,
            column=0,
            padx=10,
            pady=(5, 8),
            sticky="w",
        )

        header_revenue_label = tk.Label(
            self.revenue_frame,
            text="Revenue (CAD)",
            font=("Arial", 10, "bold"),
            width=15,
        )
        header_revenue_label.grid(
            row=0,
            column=1,
            padx=10,
            pady=(5, 8),
        )

        self.revenue_entries = []

        for day_offset in range(number_of_days):
            current_date = start_date + timedelta(days=day_offset)

            date_label = tk.Label(
                self.revenue_frame,
                text=current_date.strftime(
                    "%A, %B %d, %Y"
                ),
                font=("Arial", 10),
                anchor="w",
                width=30,
            )
            date_label.grid(
                row=day_offset + 1,
                column=0,
                padx=10,
                pady=4,
                sticky="w",
            )

            revenue_entry = tk.Entry(self.revenue_frame, width=16, justify="right")
            revenue_entry.grid(
                row=day_offset + 1,
                column=1,
                padx=10,
                pady=4,
            )

            self.revenue_entries.append(
                {
                    "date": current_date,
                    "entry": revenue_entry,
                }
            )

        self.period_label.config(
            text=(
                f"Calculation period: "
                f"{start_date.strftime('%B %d, %Y')} to "
                f"{end_date.strftime('%B %d, %Y')} "
                f"({number_of_days} days)"
            )
        )

        if self.revenue_entries:
            self.revenue_entries[0]["entry"].focus()

        self.canvas.yview_moveto(0)

    def calculate(self):
        """Calculate and display statistics for the generated period."""
        try:
            revenues = self.get_revenue_values()

            number_of_days = count_values(revenues)
            total_revenue = calculate_sum(revenues)
            mean = calculate_mean(revenues)
            standard_deviation = (population_standard_deviation(revenues))

            start_date = self.revenue_entries[0]["date"]
            end_date = self.revenue_entries[number_of_days - 1]["date"]

            self.period_result.set(
                f"{start_date.strftime('%B %d, %Y')} to "
                f"{end_date.strftime('%B %d, %Y')}"
            )
            self.days_result.set(str(number_of_days))
            self.total_result.set(f"${total_revenue:.2f} CAD")
            self.mean_result.set(f"${mean:.2f} CAD")
            self.standard_deviation_result.set(
                f"${standard_deviation:.2f} CAD"
            )

        except (InvalidDayCountError, InvalidNumberError, NegativeValueError) as error:
            messagebox.showerror("Calculation Error", str(error))

    def clear_revenue_values(self):
        """Clear entered revenues while keeping the generated dates."""
        if count_values(self.revenue_entries) == 0:
            messagebox.showinfo(
                "No Generated Period",
                "Generate the calculation period before clearing revenue values.",
            )
            return

        for revenue_item in self.revenue_entries:
            revenue_item["entry"].delete(0, tk.END)

        self.clear_results()

        self.revenue_entries[0]["entry"].focus()

    def clear_revenue_frame(self):
        """Remove all widgets from the generated revenue area."""
        for widget in self.revenue_frame.winfo_children():
            widget.destroy()

        self.revenue_entries = []

    def clear_generated_days(self):
        """Clear generated dates and restore the placeholder message."""
        self.clear_revenue_frame()

        placeholder_label = tk.Label(
            self.revenue_frame,
            text=("Select a start date and number of days, then click Generate Days."),
            font=("Arial", 10),
        )
        placeholder_label.pack(pady=30)

        self.period_label.config(text="No calculation period generated.")

        self.clear_results()

    def clear_results(self):
        """Restore the result display to its initial state."""
        self.period_result.set("No calculation has been performed.")
        self.days_result.set("—")
        self.total_result.set("—")
        self.mean_result.set("—")
        self.standard_deviation_result.set("—")

    def update_scroll_region(self, _event):
        """Update the canvas scrollable region."""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def resize_revenue_frame(self, event):
        """Resize the inner frame to match the canvas width."""
        self.canvas.itemconfigure(self.canvas_window, width=event.width,)

    def run(self):
        """Start the Tkinter application loop."""
        self.window.mainloop()