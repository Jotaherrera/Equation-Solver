import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
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
        self.nRVar = tk.BooleanVar()
        self.secanteVar = tk.BooleanVar()
        self.steffensenVar = tk.BooleanVar()

        # Create widgets
        self.setup_widgets()

    # Function to setup widgets on the app
    def setup_widgets(self):
        # Equation Entry Frame
        self.entryFrame = ttk.LabelFrame(
            self, text="Ingrese el Polinomio", padding=(20, 10)
        )
        self.entryFrame.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
        self.entryFrame.columnconfigure(index=0, weight=1)

        # Equation Entry
        self.eqEntry = ttk.Entry(self.entryFrame)
        self.eqEntry.grid(row=0, column=0, padx=5, pady=(10, 10), sticky="ew")

        # Derivative Equation
        self.derivativeEntry = ttk.Entry(self.entryFrame)
        self.derivativeEntry.grid(row=1, column=0, padx=5, pady=(10, 10), sticky="ew")

        # set a placeholder text
        self.derivativeEntry.insert(0, "Derivative Equation")
        # make the Entry widget uneditable
        self.derivativeEntry.configure(state="disabled")

        # set the font of the Entry widget to have reduced opacity and italicized text
        self.derivativeEntry.configure(font=("", 9, "italic"), foreground="#BBBBBB")

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
        self.biseccionCheck.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")

        self.reglaFalsaCheck = ttk.Checkbutton(
            self.check_frame, text="Regla Falsa", variable=self.reglaFalsaVar
        )
        self.reglaFalsaCheck.grid(row=0, column=2, padx=5, pady=10, sticky="nsew")

        self.nRCheck = ttk.Checkbutton(
            self.check_frame, text="N. R", variable=self.nRVar
        )
        self.nRCheck.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

        self.secanteCheck = ttk.Checkbutton(
            self.check_frame, text="Secante", variable=self.secanteVar
        )
        self.secanteCheck.grid(row=1, column=1, padx=5, pady=10, sticky="nsew")

        self.steffensenCheck = ttk.Checkbutton(
            self.check_frame, text="Steffensen", variable=self.steffensenVar
        )
        self.steffensenCheck.grid(row=1, column=2, padx=5, pady=10, sticky="nsew")

        # Method, Answers and Iteration Frame
        self.answersFrame = ttk.LabelFrame(
            self,
            text="    Método                    Respuestas              Prom. Iteraciones  ",
            padding=(20, 10),
        )
        self.answersFrame.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

        # Method Label
        self.tanteoLabel = ttk.Label(self.answersFrame, text="Tanteo")
        self.tanteoLabel.grid(row=0, column=0, pady=10, columnspan=2, sticky="nsew")

        self.biseccionLabel = ttk.Label(self.answersFrame, text="Bisección")
        self.biseccionLabel.grid(row=1, column=0, pady=10, columnspan=2, sticky="nsew")

        self.reglaFalsaLabel = ttk.Label(self.answersFrame, text="R. Falsa")
        self.reglaFalsaLabel.grid(row=2, column=0, pady=10, columnspan=2, sticky="nsew")

        self.nRLabel = ttk.Label(self.answersFrame, text="N. R")
        self.nRLabel.grid(row=3, column=0, pady=10, columnspan=2, sticky="nsew")

        self.secanteLabel = ttk.Label(self.answersFrame, text="Secante")
        self.secanteLabel.grid(row=4, column=0, pady=10, columnspan=2, sticky="nsew")

        self.steffensenLabel = ttk.Label(self.answersFrame, text="Steffensen")
        self.steffensenLabel.grid(row=5, column=0, pady=10, columnspan=2, sticky="nsew")

        # Inside Answer Frame
        self.insideAnswerFrame = ttk.Frame(self.answersFrame)
        self.insideAnswerFrame.grid(row=0, column=2, padx=10, sticky="nsew", rowspan=7)
        self.insideAnswerFrame.columnconfigure(index=0, weight=1)

        # Answer Outputs
        self.tanteoOutput = ttk.Entry(self.insideAnswerFrame, width=20)
        self.tanteoOutput.grid(row=0, column=0, padx=(10, 0), pady=(8, 0), sticky="ew")

        self.tanteoIterationsOutput = ttk.Entry(self.insideAnswerFrame, width=13)
        self.tanteoIterationsOutput.grid(
            row=0, column=1, padx=(10, 0), pady=(10, 0), sticky="ew"
        )

        self.biseccionOutput = ttk.Entry(self.insideAnswerFrame, width=20)
        self.biseccionOutput.grid(
            row=1, column=0, padx=(10, 0), pady=(8, 0), sticky="ew"
        )

        self.biseccionIterationsOutput = ttk.Entry(self.insideAnswerFrame, width=10)
        self.biseccionIterationsOutput.grid(
            row=1, column=1, padx=(10, 0), pady=(8, 0), sticky="ew"
        )

        self.reglaFalsaOutput = ttk.Entry(self.insideAnswerFrame, width=20)
        self.reglaFalsaOutput.grid(
            row=2, column=0, padx=(10, 0), pady=(8, 0), sticky="ew"
        )

        self.reglaFalsaIterationsOutput = ttk.Entry(self.insideAnswerFrame, width=10)
        self.reglaFalsaIterationsOutput.grid(
            row=2, column=1, padx=(10, 0), pady=(8, 0), sticky="ew"
        )

        self.nROutput = ttk.Entry(self.insideAnswerFrame, width=20)
        self.nROutput.grid(row=3, column=0, padx=(10, 0), pady=(8, 0), sticky="ew")

        self.nRIterationsOutput = ttk.Entry(self.insideAnswerFrame, width=10)
        self.nRIterationsOutput.grid(
            row=3, column=1, padx=(10, 0), pady=(8, 0), sticky="ew"
        )

        self.secanteOutput = ttk.Entry(self.insideAnswerFrame, width=20)
        self.secanteOutput.grid(row=4, column=0, padx=(10, 0), pady=(8, 0), sticky="ew")

        self.secanteIterationsOutput = ttk.Entry(self.insideAnswerFrame, width=10)
        self.secanteIterationsOutput.grid(
            row=4, column=1, padx=(10, 0), pady=(8, 0), sticky="ew"
        )

        self.steffensenOutput = ttk.Entry(self.insideAnswerFrame, width=20)
        self.steffensenOutput.grid(
            row=6, column=0, padx=(10, 0), pady=(8, 0), sticky="ew"
        )

        self.steffensenIterationsOutput = ttk.Entry(self.insideAnswerFrame, width=10)
        self.steffensenIterationsOutput.grid(
            row=6, column=1, padx=(10, 0), pady=(8, 0), sticky="ew"
        )

        # Solve Button
        self.buttonFrame = ttk.Frame(self)
        self.buttonFrame.grid(row=3, column=0, padx=20, pady=(5, 20), sticky="nsew")
        self.buttonFrame.columnconfigure(index=0, weight=1)
        self.buttonFrame.columnconfigure(index=1, weight=1)

        self.solveButton = ttk.Button(
            self.buttonFrame,
            text="Resolver",
            style="Accent.TButton",
            command=self.solve,
        )
        self.solveButton.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        # Report button
        self.reportButton = ttk.Button(
            self.buttonFrame,
            text="Reporte",
            style="Accent.TButton",
            command=self.solve,
        )
        self.reportButton.grid(row=0, column=1, padx=(5, 0), pady=0, sticky="nsew")

        # Graph Frame
        self.graphFrame = ttk.Frame(self)
        self.graphFrame.grid(row=0, column=1, padx=(0, 20), pady=(25, 10), rowspan=5)

        # Graph
        self.fig = Figure(figsize=(4.7, 5.6), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.fig.tight_layout()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graphFrame)

        # Setting the predefined zoom
        self.ax.set_xlim(-50, 50)
        self.ax.set_ylim(-50, 50)

        # Drawing the canvas
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")

        # Drawing x and y axes
        self.ax.axhline(0, color="black", linewidth="1.5")
        self.ax.axvline(0, color="black", linewidth="1.5")

        # Navigation Bar
        self.tlb = NavigationToolbar2Tk(
            self.canvas, self.graphFrame, pack_toolbar=False
        )
        self.tlb.update()
        self.tlb.grid(row=1, column=0, sticky="nsew")

        # Connecting the scrolling action
        self.fig.canvas.mpl_connect("scroll_event", self.on_scroll)

        # Set the cross as the initial element
        self.tlb.pan()

    # Function to scroll with the mouse
    def on_scroll(self, event):
        # Get limits
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()

        # Calculate scroll limits
        if event.button == "up":
            # Zoom in
            x_center = (xlim[0] + xlim[1]) / 2
            y_center = (ylim[0] + ylim[1]) / 2
            x_range = (xlim[1] - xlim[0]) / 2
            y_range = (ylim[1] - ylim[0]) / 2
            self.ax.set_xlim(x_center - x_range / 2, x_center + x_range / 2)
            self.ax.set_ylim(y_center - y_range / 2, y_center + y_range / 2)
        elif event.button == "down":
            # Zoom out
            x_center = (xlim[0] + xlim[1]) / 2
            y_center = (ylim[0] + ylim[1]) / 2
            x_range = (xlim[1] - xlim[0]) * 2
            y_range = (ylim[1] - ylim[0]) * 2
            self.ax.set_xlim(x_center - x_range / 2, x_center + x_range / 2)
            self.ax.set_ylim(y_center - y_range / 2, y_center + y_range / 2)

        self.fig.canvas.draw()

    # Mother function bound to the button
    def solve(self):
        self.solveButton.config(state=tk.DISABLED)
        self.reportButton.config(state=tk.DISABLED)
        self.tanteoCheck.config(state=tk.DISABLED)
        self.biseccionCheck.config(state=tk.DISABLED)
        self.reglaFalsaCheck.config(state=tk.DISABLED)
        self.nRCheck.config(state=tk.DISABLED)
        self.secanteCheck.config(state=tk.DISABLED)
        self.steffensenCheck.config(state=tk.DISABLED)

        self.popup = self.show_popup()

        # Get the entry
        eqVar, degree = self.getEntry()

        # Check if there is something on the entry
        if eqVar is not None and eqVar != "":
            zeros = self.checked()
            self.getGraphic(eqVar, zeros)

        self.popup.destroy()
        self.solveButton.config(state=tk.NORMAL)
        self.reportButton.config(state=tk.NORMAL)
        self.tanteoCheck.config(state=tk.NORMAL)
        self.biseccionCheck.config(state=tk.NORMAL)
        self.reglaFalsaCheck.config(state=tk.NORMAL)
        self.nRCheck.config(state=tk.NORMAL)
        self.secanteCheck.config(state=tk.NORMAL)
        self.steffensenCheck.config(state=tk.NORMAL)

    # Show a loading popup
    def show_popup(self):
        self.popup = tk.Toplevel()
        self.popup.title("Cargando...")
        self.popup.geometry("200x100")

        ttk.Label(self.popup, text="Cargando...").pack(pady=10)
        ttk.Progressbar(self.popup, mode="indeterminate").pack(pady=10)
        self.popup.transient(master=self)
        self.popup.grab_set()

        self.popup.update()
        self.popup.minsize(self.popup.winfo_width(), self.popup.winfo_height())
        x_cordinate = int(
            (self.popup.winfo_screenwidth() / 2) - (self.popup.winfo_width() / 2)
        )
        y_cordinate = int(
            (self.popup.winfo_screenheight() / 2) - (self.popup.winfo_height() / 2)
        )
        self.popup.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))
        self.popup.update()
        return self.popup

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

        self.nROutput.configure(state="normal")
        self.nRIterationsOutput.configure(state="normal")
        self.nROutput.delete(0, "end")
        self.nRIterationsOutput.delete(0, "end")

        self.secanteOutput.configure(state="normal")
        self.secanteIterationsOutput.configure(state="normal")
        self.secanteOutput.delete(0, "end")
        self.secanteIterationsOutput.delete(0, "end")

        self.steffensenOutput.configure(state="normal")
        self.steffensenIterationsOutput.configure(state="normal")
        self.steffensenOutput.delete(0, "end")
        self.steffensenIterationsOutput.delete(0, "end")

    # Function to check which function/s is/are selected
    def checked(self):
        # Reset states
        self.cleanEntries()

        if self.tanteoVar.get() == True:
            zeros = self.tanteo()
        if self.biseccionVar.get() == True:
            zeros = self.biseccion()
        if self.reglaFalsaVar.get() == True:
            zeros = self.reglaFalsa()
        if self.nRVar.get() == True:
            zeros = self.nR()
        if self.secanteVar.get() == True:
            zeros = self.secante()
        if self.steffensenVar.get() == True:
            zeros = self.steffensen()

        return zeros

    # Function to get the entry equation
    def getEntry(self):
        # Get equation from entry box
        rawEq = str(self.eqEntry.get())
        # Change x for xI
        eqVar = rawEq.replace("x", "xI").replace("X", "xI")

        # Get equation degree
        match = re.search(r"\*\*?\s*(\d+)", str(eqVar))
        if match:
            degree = int(match.group(1))
        else:
            degree = 1

        if (degree % 2) == 0:
            eqVar = re.sub(r"xI\*\*([02468])", r"abs(xI)**\1", eqVar)

        return eqVar, degree

    # Function to generate the random numbers for biseccion and regla falsa
    def rndNumbers(self, eqVar, roots):
        xLow = rnd.randint(-100, 100)
        while eval(eqVar, {"xI": xLow}) > 0 and xLow not in roots:
            xLow = rnd.randint(-100, 100)

        xHigh = rnd.randint(-100, 100)
        while eval(eqVar, {"xI": xHigh}) < 0 and xHigh not in roots:
            xHigh = rnd.randint(-100, 100)

        return xLow, xHigh

    # Function to get an integer seed
    def getIntSeed(self, roots):
        while True:
            x0 = rnd.randint(-10, 10)
            if x0 not in roots:
                return x0

    # Function to get a float seed
    def getUniformSeed(self, roots):
        while True:
            x0 = rnd.uniform(-10, 10)
            if x0 not in roots:
                return x0

    # Function to verify if the root is already in the array
    def verifyRoots(self, roots, counters, num, count):
        if round(num, 2) not in roots:
            roots.append(round(num, 2))
            counters.append(count)

    # Function to clean the array from numbers that are to close
    def cleanArray(self, arr, margin):
        return sorted(
            [arr[0]]
            + [arr[i] for i in range(1, len(arr)) if abs(arr[i] - arr[i - 1]) > margin]
        )

    # Function to print the answers in the UI
    def giveAnswers(self, methodOutput, methodIterationsOutput, roots, counters):
        averageCounter = sum(counters) / len(counters)
        methodOutput.insert(0, sorted(roots))
        methodOutput.configure(state="readonly")
        methodIterationsOutput.insert(0, averageCounter)
        methodIterationsOutput.configure(state="readonly")

    def tanteo(self):
        roots = []
        counters = []

        # Get equation entry
        eqVar, degree = self.getEntry()

        bigCount = 0
        while len(roots) < degree:
            bigCount += 1
            counter = 0

            # Generating random number
            x1 = 0
            xI = self.getIntSeed(roots)

            if xI >= 0:  # if xI is positive or zero
                while True:
                    if eval(eqVar, {"xI": xI}) > 0:
                        counter += 1
                        x1 = xI - 0.001
                        xI = x1
                    elif eval(eqVar, {"xI": xI}) < 0:
                        counter += 1
                        x1 = xI + 0.001

                    if abs(eval(eqVar, {"xI": xI})) <= 0.0001:
                        self.verifyRoots(roots, counters, xI, counter)
                        break

                    if counter > 1000:
                        break

            else:  # if xI is negative
                while True:
                    if eval(eqVar, {"xI": xI}) > 0:
                        counter += 1
                        x1 = xI + 0.001
                        xI = x1
                    elif eval(eqVar, {"xI": xI}) < 0:
                        counter += 1
                        x1 = xI - 0.001
                        xI = x1

                    if abs(eval(eqVar, {"xI": xI})) <= 0.0001:
                        self.verifyRoots(roots, counters, xI, counter)
                        break

                    if counter > 1000:
                        break
            if bigCount > 200:
                if len(roots) == 0:
                    messagebox.showinfo(
                        title="Info",
                        message="Se supero el número de iteraciones por tanteo, no se pudo resolver por este método.",
                    )
                    return roots
                break

        roots = self.cleanArray(roots, 0.1)
        self.giveAnswers(
            self.tanteoOutput, self.tanteoIterationsOutput, roots, counters
        )

        return roots

    def biseccion(self):
        roots = []
        counters = []
        bigCount = 0
        eqVar, degree = self.getEntry()
        while len(roots) < degree:
            bigCount += 1
            counter = 0
            xLow, xHigh = self.rndNumbers(eqVar, roots)

            while True:
                counter += 1
                xMiddle = (xHigh + xLow) / 2

                if eval(eqVar, {"xI": xMiddle}) > 0:
                    xHigh = xMiddle
                else:
                    xLow = xMiddle

                if abs(eval(eqVar, {"xI": xMiddle})) <= 0.0001:
                    self.verifyRoots(roots, counters, xMiddle, counter)
                    break

                if counter > 10000:
                    break
            if bigCount > 500:
                break
        roots = self.cleanArray(roots, 0.1)
        self.giveAnswers(
            self.biseccionOutput, self.biseccionIterationsOutput, roots, counters
        )

        return roots

    def reglaFalsa(self):
        eqVar, degree = self.getEntry()

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

    def newtonRaphson(self):
        pass

    def secante(self):
        pass

    def steffensen(self):
        counters = []
        roots = []

        eQ, degree = self.getEntry()
        bigCount = 0

        while len(roots) < degree:
            bigCount += 1
            count = 0
            x0 = self.getUniformSeed(roots)

            while True:
                count += 1

                if abs(eval(eQ, {"xI": x0})) <= 0.0001:
                    self.verifyRoots(roots, counters, x0, count)
                    break
                else:
                    eqX0PlusEqX0 = eQ.replace("xI", str(x0 + eval(eQ, {"xI": x0})))

                    x1 = x0 - (
                        (eval(eQ, {"xI": x0}) ** 2)
                        / (eval(eqX0PlusEqX0) - eval(eQ, {"xI": x0}))
                    )

                    if abs(eval(eQ, {"xI": x1})) <= 0.0001:
                        self.verifyRoots(roots, counters, x1, count)
                        break
                    else:
                        x0 = x1

                    if count > 1000:
                        break
            if bigCount > 200:
                if len(roots) == 0:
                    messagebox.showinfo(
                        title="Info",
                        message="Se supero el número de iteraciones por tanteo, no se pudo resolver por este método.",
                    )
                    return roots
                break

        roots = self.cleanArray(roots, 0.1)
        self.giveAnswers(
            self.steffensenOutput, self.steffensenIterationsOutput, roots, counters
        )
        return roots

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
            return eval(eqVar, {"xI": x})

        # Restart the graph to its initial state
        restart()

        # Defining the range for x
        x = range(-1000, 1000)
        # List comprehension fro the range of y
        y = [f(i) for i in x]
        # Drawing the plot
        self.ax.plot(x, y)
        # Draw the red point
        if len(zeros) != 0:
            for zero in zeros:
                self.ax.scatter(zero, 0, color="red", zorder=10)
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
    root.resizable(True, True)

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
