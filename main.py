import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from math import *
import random as rnd
import re


class App(ttk.Frame):
    # Construction method
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        # Create control variables for checkboxes
        self.tanteoVar = tk.BooleanVar()
        self.biseccionVar = tk.BooleanVar()
        self.reglaFalsaVar = tk.BooleanVar()

        # Create widgets
        self.setup_widgets()

    # Function to setup widgets on the app
    def setup_widgets(self):
        # Equation Entry Frame
        self.entryFrame = ttk.LabelFrame(
            self, text="Ingrese el Polinomio", padding=(20, 10)
        )
        self.entryFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.entryFrame.columnconfigure(index=0, weight=1)

        # Equation Entry
        self.eqEntry = ttk.Entry(self.entryFrame)
        self.eqEntry.grid(row=0, column=0, padx=5, pady=(10, 10), sticky="ew")

        # Create a Frame for the Checkbuttons
        self.check_frame = ttk.LabelFrame(
            self, text="Elige el método", padding=(20, 10)
        )
        self.check_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        # Checkbuttons
        self.tanteoCheck = ttk.Checkbutton(
            self.check_frame, text="Tanteo", variable=self.tanteoVar
        )
        self.tanteoCheck.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

        self.biseccionCheck = ttk.Checkbutton(
            self.check_frame, text="Bisección", variable=self.biseccionVar
        )
        self.biseccionCheck.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

        self.reglaFalsaCheck = ttk.Checkbutton(
            self.check_frame, text="Regla Falsa", variable=self.reglaFalsaVar
        )
        self.reglaFalsaCheck.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")

        # Method, Answers and Iteration Frame
        self.answersFrame = ttk.LabelFrame(
            self,
            text="    Método          Respuesta        Iteraciones         ",
            padding=(20, 10),
        )
        self.answersFrame.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

        # Method Label
        self.tanteoLabel = ttk.Label(self.answersFrame, text="Tanteo")
        self.tanteoLabel.grid(row=0, column=0, pady=10, columnspan=2, sticky="nsew")

        self.biseccionLabel = ttk.Label(self.answersFrame, text="Bisección")
        self.biseccionLabel.grid(row=1, column=0, pady=10, columnspan=2, sticky="nsew")

        self.reglaFalsaLabel = ttk.Label(self.answersFrame, text="R. Falsa")
        self.reglaFalsaLabel.grid(row=2, column=0, pady=10, columnspan=2, sticky="nsew")

        # Inside Answer Frame
        self.insideAnswerFrame = ttk.Frame(self.answersFrame)
        self.insideAnswerFrame.grid(row=0, column=2, padx=10, sticky="nsew", rowspan=3)
        self.insideAnswerFrame.columnconfigure(index=0, weight=1)

        # Answer Outputs
        self.tanteoOutput = ttk.Entry(self.insideAnswerFrame, width=10)
        self.tanteoOutput.grid(row=0, column=0, padx=(10, 0), pady=(8, 0), sticky="ew")

        self.tanteoIterationsOutput = ttk.Entry(self.insideAnswerFrame, width=10)
        self.tanteoIterationsOutput.grid(
            row=0, column=1, padx=(10, 0), pady=(8, 0), sticky="ew"
        )

        self.biseccionOutput = ttk.Entry(self.insideAnswerFrame, width=10)
        self.biseccionOutput.grid(
            row=1, column=0, padx=(10, 0), pady=(8, 0), sticky="ew"
        )

        self.biseccionIterationsOutput = ttk.Entry(self.insideAnswerFrame, width=10)
        self.biseccionIterationsOutput.grid(
            row=1, column=1, padx=(10, 0), pady=(8, 0), sticky="ew"
        )

        self.reglaFalsaOutput = ttk.Entry(self.insideAnswerFrame, width=10)
        self.reglaFalsaOutput.grid(
            row=2, column=0, padx=(10, 0), pady=(8, 0), sticky="ew"
        )

        self.reglaFalsaIterationsOutput = ttk.Entry(self.insideAnswerFrame, width=10)
        self.reglaFalsaIterationsOutput.grid(
            row=2, column=1, padx=(10, 0), pady=(8, 0), sticky="ew"
        )

        # Solve Button
        self.buttonFrame = ttk.Frame(self)
        self.buttonFrame.grid(row=3, column=0, padx=20, pady=(5, 20), sticky="nsew")
        self.buttonFrame.columnconfigure(index=0, weight=1)

        self.accentbutton = ttk.Button(
            self.buttonFrame,
            text="Resolver",
            style="Accent.TButton",
            command=self.solve,
        )
        self.accentbutton.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        # Graph Frame
        self.graphFrame = ttk.Frame(self)
        self.graphFrame.grid(row=0, column=1, padx=(0, 20), pady=(30, 10), rowspan=4)
        self.graphFrame.columnconfigure(index=0, weight=1)

        # Graph
        self.fig = Figure(figsize=(4, 5.2), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.fig.tight_layout()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graphFrame)

        # Setting the predefined zoom
        self.ax.set_xlim(-50, 50)
        self.ax.set_ylim(-50, 50)

        # Drawing the canvas
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

        # Drawing x and y axes
        self.ax.axhline(0, color="black", linewidth="1.5")
        self.ax.axvline(0, color="black", linewidth="1.5")

        # Navigation Bar
        self.tlb = NavigationToolbar2Tk(self.canvas, self.graphFrame)
        self.tlb.update()
        self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

        # Connecting the scrolling action
        self.fig.canvas.mpl_connect("scroll_event", self.on_scroll)

        # Set the cross as the initial element
        self.tlb.pan()

    # Function to scroll with the mouse
    def on_scroll(self, event):
        # get the current x and y limits of the plot
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()

        # calculate the new x and y limits based on the scroll direction
        if event.button == "up":
            # zoom in
            x_center = (xlim[0] + xlim[1]) / 2
            y_center = (ylim[0] + ylim[1]) / 2
            x_range = (xlim[1] - xlim[0]) / 2
            y_range = (ylim[1] - ylim[0]) / 2
            self.ax.set_xlim(x_center - x_range / 2, x_center + x_range / 2)
            self.ax.set_ylim(y_center - y_range / 2, y_center + y_range / 2)
        elif event.button == "down":
            # zoom out
            x_center = (xlim[0] + xlim[1]) / 2
            y_center = (ylim[0] + ylim[1]) / 2
            x_range = (xlim[1] - xlim[0]) * 2
            y_range = (ylim[1] - ylim[0]) * 2
            self.ax.set_xlim(x_center - x_range / 2, x_center + x_range / 2)
            self.ax.set_ylim(y_center - y_range / 2, y_center + y_range / 2)

        # redraw the plot
        self.fig.canvas.draw()

    # Mother function bound to the button
    def solve(self):
        # Get the entry
        eqVar = self.getEntry()

        # Check if there is something on the entry
        if eqVar is not None and eqVar != "":
            zero = self.checked()
            self.getGraphic(eqVar, zero)

    # Function to clear the entries
    def cleanEntries(self):
        # Reset states
        self.tanteoOutput.configure(state="normal")
        self.tanteoIterationsOutput.configure(state="normal")
        self.tanteoOutput.delete(0, "end")
        self.tanteoIterationsOutput.delete(0, "end")

        self.biseccionOutput.configure(state="normal")
        self.biseccionIterationsOutput.configure(state="normal")
        self.biseccionOutput.delete(0, "end")
        self.biseccionIterationsOutput.delete(0, "end")

        self.reglaFalsaOutput.configure(state="normal")
        self.reglaFalsaIterationsOutput.configure(state="normal")
        self.reglaFalsaOutput.delete(0, "end")
        self.reglaFalsaIterationsOutput.delete(0, "end")

    # Function to check which function/s is/are selected
    def checked(self):
        # Reset states
        self.cleanEntries()

        if self.tanteoVar.get() == True:
            zero = self.tanteo()
        if self.biseccionVar.get() == True:
            zero = self.biseccion()
        if self.reglaFalsaVar.get() == True:
            zero = self.reglaFalsa()

        return zero

    # Function to get the entry equation
    def getEntry(self):
        # Get equation from entry box
        rawEq = str(self.eqEntry.get())
        # Change x for xI
        eqVar = rawEq.replace("x", "xI").replace("X", "xI")
        # Wrap every x raised to square power in abs()
        eqVar = re.sub(r"xI\*\*([02468])", r"abs(xI)**\1", eqVar)
        return eqVar

    # Function to generate the random numbers for biseccion and regla falsa
    def rndNumbers(self, eqVar):
        # Get a random low value
        xLow = rnd.randint(-100, 100)
        # Replace random values in the equation
        equationLow = eqVar.replace("xI", str(xLow))
        while eval(equationLow) > 0:
            xLow = rnd.randint(-100, 100)
            equationLow = eqVar.replace("xI", str(xLow))

        # Get a random high value
        xHigh = rnd.randint(xLow, 100)
        # Replace random values in the equation
        equationHigh = eqVar.replace("xI", str(xHigh))
        while eval(equationHigh) < 0:
            xHigh = rnd.randint(xLow, 100)
            equationHigh = eqVar.replace("xI", str(xHigh))

        return xLow, xHigh

    def tanteo(self):
        # Get equation entry
        eqVar = self.getEntry()

        # Generating random number
        xI = rnd.randint(-100, 100)

        # Initial replacing
        eq = eqVar.replace("xI", str(xI))

        counter = 0
        if xI >= 0:  # if xI is positive or zero
            while True:
                if eval(eq) > 0:
                    counter += 1
                    x1 = xI - 0.001
                    xI = x1
                    eq = eqVar.replace("xI", str(xI))
                elif eval(eq) < 0:
                    counter += 1
                    x1 = xI + 0.001
                    xI = x1
                    eq = eqVar.replace("xI", str(xI))

                if abs(eval(eq)) <= 0.001:
                    self.tanteoOutput.insert(0, round(xI, 2))
                    self.tanteoOutput.configure(state="readonly")
                    self.tanteoIterationsOutput.insert(0, counter)
                    self.tanteoIterationsOutput.configure(state="readonly")
                    return xI

        else:  # if xI is negative
            while True:
                if eval(eq) > 0:
                    counter += 1
                    x1 = xI + 0.001
                    xI = x1
                    eq = eqVar.replace("xI", str(xI))
                elif eval(eq) < 0:
                    counter += 1
                    x1 = xI - 0.001
                    xI = x1
                    eq = eqVar.replace("xI", str(xI))

                if abs(eval(eq)) <= 0.001:
                    self.tanteoOutput.insert(0, round(xI, 2))
                    self.tanteoOutput.configure(state="readonly")
                    self.tanteoIterationsOutput.insert(0, counter)
                    self.tanteoIterationsOutput.configure(state="readonly")
                    return xI

    def biseccion(self):
        # Get entry
        eqVar = self.getEntry()

        # Get random numbers
        xLow, xHigh = self.rndNumbers(eqVar)

        counter = 0
        while True:
            counter += 1
            xMiddle = (xHigh + xLow) / 2

            eq = eqVar.replace("xI", str(xMiddle))

            if eval(eq) > 0:
                xHigh = xMiddle
            else:
                xLow = xMiddle

            if abs(eval(eq)) <= 0.001:
                self.biseccionOutput.insert(0, round(xMiddle, 2))
                self.biseccionOutput.configure(state="readonly")
                self.biseccionIterationsOutput.insert(0, counter)
                self.biseccionIterationsOutput.configure(state="readonly")
                return xMiddle

    def reglaFalsa(self):
        eqVar = self.getEntry()

        xLow, xHigh = self.rndNumbers(eqVar)

        counter = 0
        while True:
            counter += 1

            equationLow = eqVar.replace("xI", str(xLow))
            equationHigh = eqVar.replace("xI", str(xHigh))

            xMiddle = xLow - (
                eval(equationLow)
                * (xHigh - xLow)
                / (eval(equationHigh) - eval(equationLow))
            )
            eqM = eqVar.replace("xI", str(xMiddle))

            if eval(eqM) > 0:
                xHigh = xMiddle
            else:
                xLow = xMiddle

            if abs(eval(eqM)) <= 0.001:
                self.reglaFalsaOutput.insert(0, round(xMiddle, 2))
                self.reglaFalsaOutput.configure(state="readonly")
                self.reglaFalsaIterationsOutput.insert(0, counter)
                self.reglaFalsaIterationsOutput.configure(state="readonly")
                return xMiddle

    # Function make the graphic based on the function
    def getGraphic(self, eqVar, zeros):
        def restart():
            self.ax.clear()
            self.ax.set_xlim(-50, 50)
            self.ax.set_ylim(-50, 50)
            self.ax.axhline(0, color="black", linewidth="1.5")
            self.ax.axvline(0, color="black", linewidth="1.5")
            self.canvas.draw()

        # Graph function
        def f(x):
            return eval(eqVar.replace("xI", str(x)))

        # Restart the graph to its initial state
        restart()

        # Defining the range for x
        x = range(-1000, 1000)
        # List comprehension fro the range of y
        y = [f(i) for i in x]
        # Drawing the plot
        self.ax.plot(x, y)
        # Draw the red point
        self.ax.scatter(zeros, 0, color="red", zorder=10)
        # Showing plot and updating canvas
        plt.show()
        self.canvas.draw()


# Python entry Point
if __name__ == "__main__":
    # Shortcut name to call tkinter
    root = tk.Tk()

    # App name
    root.title("Equation Solver")

    # Making resizable or not
    root.resizable(False, False)

    # Graph style
    style.use("fivethirtyeight")

    # App theme
    root.tk.call("source", "./src/Tk Theme/azure.tcl")
    root.tk.call("set_theme", "dark")

    # App icon
    root.iconbitmap("./public/images/sine.ico")

    # Instancing object
    app = App(root)
    app.pack(fill="both", expand=True)

    # Always appear on screen center
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))

    # Main loop function
    root.mainloop()
