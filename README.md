# Equation Solver

![Principal Screen Picture](https://github.com/Jotaherrera/Equation-Solver/blob/main/public/github/ppScreen.png)

Equation Solver is a tool built using Python and Tkinter that allows users to solve algebraic equations. It serves as a graphic calculator for any function from grade one to eight, and this limit is easily modifiable. The tool uses different methods to solve equations:

- **Trial and Error:** This method adds or subtracts until it reaches the solution(s).
- **Bisection:** This method involves repeatedly bisecting the interval in which the solution resides.
- **Regula Falsi:** This method approximates the solution(s) by linear interpolation between the values of the function at the endpoints of an interval.
- **Secant:** This method approximates the solution(s) by using a line that passes through two points on the graph of the function.
- **Newton-Raphson:** This method approximates the solution(s) by using the function and its derivative to iteratively improve an initial guess.
- **Steffensen:** This method approximates the solution(s) by using a fixed point iteration method with an additional acceleration step using the function's second derivative.

All methods use a random generation function to get the initial numbers of the calculation, like a starting point.

## Technologies

Equation Solver was built using the following technologies:

- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Python](https://www.python.org/)
- [Tcl](https://www.tcl.tk/)

## Libraries

The following libraries were used in the development of Equation Solver:

- `tkinter`: A standard GUI library for Python.
- `ttk`: An extension of the `tkinter` module, providing themed widgets.
- `messagebox`: A module from `tkinter` that provides message boxes for displaying information or getting user input.
- `matplotlib`: A plotting library for Python.
- `matplotlib.figure`: A module for creating `Figure` instances.
- `matplotlib.style`: A module that provides styles for `matplotlib` plots.
- `matplotlib.backends.backend_tkagg`: A module that provides the `FigureCanvasTkAgg` class, which is used for embedding `matplotlib` plots into `tkinter` GUIs.
- `matplotlib.backends._backend_tk`: A module that provides the `NavigationToolbar2Tk` class, which is used for adding a toolbar to `matplotlib` plots in `tkinter` GUIs.
- `math`: A module that provides mathematical functions.
- `random`: A module that provides functions for generating random numbers.
- `sympy`: A Python library for symbolic mathematics.
- `reportlab.pdfgen`: A module for generating PDF documents.
- `reportlab.lib.pagesizes`: A module that provides standard page sizes for PDF documents.
- `reportlab.lib.units`: A module that provides a unit conversion function for `reportlab`.
- `reportlab.lib.utils`: A module that provides utility functions for `reportlab`.
- `datetime`: A module that provides classes for working with dates and times.
- `os`: A module that provides a way of using operating system dependent functionality.
- `io`: A module that provides tools for working with I/O streams.
- `re`: A module that provides support for regular expressions.

## Theme

The GUI of Equation Solver uses a custom theme inspired by the Azure TTK Theme, created by [rdbende](https://github.com/rdbende). The theme provides a modern and clean look to the application and improves the user experience.

You can check out the Azure TTK Theme on [Azure theme for ttk](https://github.com/rdbende/Azure-ttk-theme).

## Prerequisites

Before running the application, please make sure that you have Python 3 installed on your computer. You can download Python from the official website [here](https://www.python.org/downloads/).

Additionally, you need to clone or download this repository to your local machine. You can do this by clicking on the "Code" button on the GitHub repository page and selecting your preferred method of download.

## Installation

It is recommended to use a virtual environment to install the required libraries and run the program. This keeps the dependencies of this project separate from other projects you may have on your system.

To create a virtual environment, follow these steps:

1. Open a terminal and navigate to the directory where you want to create the virtual environment.

2. Enter the following command:

   ```bash
   python -m venv env
   ```

   This will create a new directory called `env` in the current directory.

3. Activate the virtual environment by running the following command:

   - For Windows:

   ```bash
   env\Scripts\activate.bat
   ```

   - For Linux/Mac:

   ```bash
   source env/bin/activate
   ```

4. Install the required libraries by running the following command:

   ```bash
   pip install -r requirements.txt
   ```

This will install all the required libraries listed in the `requirements.txt` file.

## Running the Program

To run the program, make sure you have activated the virtual environment and navigate to the directory where the main.py file is located.

Then, simply run the following command in the terminal:

```bash
python main.py
```

This will start the program and open the GUI window. From there, you can use the various options and features of the program.

## Screenshots

Here are some screenshots of the Equation Solver in action:

![Screenshot 1](https://github.com/Jotaherrera/Equation-Solver/blob/main/public/github/Screenshot1.png)

![Screenshot 2](https://github.com/Jotaherrera/Equation-Solver/blob/main/public/github/Screenshot2.png)

![Screenshot 3](https://github.com/Jotaherrera/Equation-Solver/blob/main/public/github/Screenshot3.png)

![Screenshot 4](https://github.com/Jotaherrera/Equation-Solver/blob/main/public/github/Screenshot4.png)

![Screenshot 5](https://github.com/Jotaherrera/Equation-Solver/blob/main/public/github/Screenshot5.png)
