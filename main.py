import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from math import *
import random as rnd
import re


class App(ttk.Frame):
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
            command=self.tanteo,
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
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

        # Navigation Bar
        self.tlb = NavigationToolbar2Tk(self.canvas, self.graphFrame)
        self.tlb.update()
        self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

    def tanteo(self):
        # Reset states
        self.tanteoOutput.configure(state="normal")
        self.tanteoIterationsOutput.configure(state="normal")
        self.tanteoOutput.delete(0, "end")
        self.tanteoIterationsOutput.delete(0, "end")

        # Generating random number
        self.xI = rnd.randint(-100, 100)

        # Getting and replacing letter for the random number
        self.rawEq = str(self.eqEntry.get())
        self.pattern = re.compile("[a-zA-Z]")
        self.eqVar = self.pattern.sub("xI", self.rawEq)
        self.eq = self.eqVar.replace("xI", str(self.xI))

        self.count = 0
        while True:
            if eval(self.eq) > 0:
                self.count += 1
                self.x1 = self.xI - 0.01
                self.xI = self.x1
                self.eq = self.eqVar.replace("xI", str(self.xI))
                if eval(self.eq) <= 0.001:
                    self.tanteoOutput.insert(0, round(self.xI, 2))
                    self.tanteoOutput.configure(state="readonly")
                    self.tanteoIterationsOutput.insert(0, self.count)
                    self.tanteoIterationsOutput.configure(state="readonly")
                    break
            else:
                self.count += 1
                self.x1 = self.xI + 0.01
                self.xI = self.x1
                self.eq = self.eqVar.replace("xI", str(self.xI))
                if eval(self.eq) >= 0.001:
                    self.tanteoOutput.insert(0, round(self.xI, 2))
                    self.tanteoOutput.configure(state="readonly")
                    self.tanteoIterationsOutput.insert(0, self.count)
                    self.tanteoIterationsOutput.configure(state="readonly")
                    break


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

    app = App(root)
    app.pack(fill="both", expand=True)

    # Always appear on screen center
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))

    root.mainloop()
