# SOEN 6011 – Population Standard Deviation Calculator
This project implements **F8: Population Standard Deviation** in Python using the **Two-Pass Algorithm**. 
It provides a simple textual user interface for entering numerical values and calculating the population standard deviation.

**Author:** Nguyen Ha Dao  
**Student ID:** 40341491  
**Course:** SOEN 6011 – Software Engineering Processes  
**Semester:** Summer 2026

---

## Project Structure

```text
SOEN6011-F8-Population-Standard-Deviation/
├── src/
│   ├── exceptions.py
│   ├── gui.py
│   ├── main.py
│   ├── standard_deviation.py
│   └── textual_interface_archive/
│       ├── main.py
│       └── standard_deviation.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Features

- Population standard deviation calculated using the **Two-Pass Algorithm**
- Implementation developed **from scratch** (no statistical libraries)
- Tkinter graphical user interface
- Calendar-based start date selection
- User-defined calculation period (1–31 days)
- Blank revenue fields are interpreted as **0**
- Custom exception handling with helpful error messages
- Textual interface from Deliverable 1 preserved in the archive folder

---

## Requirements

- Python 3.13 or later
- Tkinter (included with the standard Python installation)

Install the required dependency:

```bash
python -m pip install -r requirements.txt
```

---

## Run the GUI

From the project root:

```bash
python src/main.py
```

---

## Run the Deliverable 1 Textual Interface (Archive)

```bash
python src/textual_interface_archive/main.py
```

---

## Example GUI Workflow

1. Select a start date.
2. Enter the number of days (1–31).
3. Click **Generate Days**.
4. Enter daily rental revenue values.
5. Leave blank days to represent **0** revenue.
6. Click **Calculate** to display:
   - Number of days
   - Total revenue
   - Average daily revenue
   - Population standard deviation