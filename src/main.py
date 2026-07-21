"""Application entry point."""

from gui import PopulationStandardDeviationGUI


def main():
    """Start the graphical user interface."""
    application = PopulationStandardDeviationGUI()
    application.run()

if __name__ == "__main__":
    main()