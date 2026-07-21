# SOEN 6011 – Population Standard Deviation Calculator
This project implements **F8: Population Standard Deviation** in Python using the **Two-Pass Algorithm**. 
It provides a simple textual user interface for entering numerical values and calculating the population standard deviation.

**Author:** Ha Dao  
**Student ID:** 40341491  
**Course:** SOEN 6011 – Software Engineering Processes  
**Semester:** Summer 2026

## Project Structure
```text
SOEN6011-F8-Population-Standard-Deviation/
├── src/
│   ├── exceptions.py
│   ├── gui.py
│   ├── main.py
│   └── standard_deviation.py
└── textual_interface_archive/
│   ├── main.py
│   └── standard_deviation.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Requirements
- Python 3.13 or later

## Install the required dependency:
```bash
python -m pip install -r requirements.txt
```

## How to Run the Textual IF (archive)
From the project root:
```bash
python src/textual_interface_archive/main.py
```

Example input:
```
100 120 80 110 90
```

Example output:
```
Population Standard Deviation Calculator
----------------------------------------
Number of revenue values: 5
Population standard deviation: 14.14
```

## How to Run the GUI
```bash
python src/main.py
```