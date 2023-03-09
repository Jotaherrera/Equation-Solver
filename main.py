import tkinter as tk
from tkinter import ttk


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        # Create value lists
        self.option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]
        self.combo_list = ["Combobox", "Editable item 1", "Editable item 2"]
        self.readonly_combo_list = ["Readonly combobox", "Item 1", "Item 2"]

        # Create control variables
        self.tanteoVar = tk.BooleanVar()
        self.biseccionVar = tk.BooleanVar()
        self.reglaFalsaVar = tk.BooleanVar()

        # Create widgets :)
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
        self.tanteoOutput = ttk.Entry(
            self.insideAnswerFrame, width=10, state=tk.DISABLED
        )
        self.tanteoOutput.grid(row=0, column=0, padx=(10, 0), pady=(8, 0), sticky="ew")

        self.tanteoIterationsOutput = ttk.Entry(
            self.insideAnswerFrame, width=10, state=tk.DISABLED
        )
        self.tanteoIterationsOutput.grid(
            row=0, column=1, padx=(10, 0), pady=(8, 0), sticky="ew"
        )

        self.biseccionOutput = ttk.Entry(
            self.insideAnswerFrame, width=10, state=tk.DISABLED
        )
        self.biseccionOutput.grid(
            row=1, column=0, padx=(10, 0), pady=(8, 0), sticky="ew"
        )

        self.biseccionIterationsOutput = ttk.Entry(
            self.insideAnswerFrame, width=10, state=tk.DISABLED
        )
        self.biseccionIterationsOutput.grid(
            row=1, column=1, padx=(10, 0), pady=(8, 0), sticky="ew"
        )

        self.reglaFalsaOutput = ttk.Entry(
            self.insideAnswerFrame, width=10, state=tk.DISABLED
        )
        self.reglaFalsaOutput.grid(
            row=2, column=0, padx=(10, 0), pady=(8, 0), sticky="ew"
        )

        self.reglaFalsaIterationsOutput = ttk.Entry(
            self.insideAnswerFrame, width=10, state=tk.DISABLED
        )
        self.reglaFalsaIterationsOutput.grid(
            row=2, column=1, padx=(10, 0), pady=(8, 0), sticky="ew"
        )

        # Solve Button
        self.buttonFrame = ttk.Frame(self)
        self.buttonFrame.grid(row=3, column=0, padx=20, pady=(5, 20), sticky="nsew")
        self.buttonFrame.columnconfigure(index=0, weight=1)

        self.accentbutton = ttk.Button(
            self.buttonFrame, text="Resolver", style="Accent.TButton"
        )
        self.accentbutton.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Equation Solver")
    root.resizable(False, False)

    root.tk.call("source", "./src/Tk Theme/azure.tcl")
    root.tk.call("set_theme", "dark")

    root.iconbitmap("./public/images/function.ico")

    app = App(root)
    app.pack(fill="both", expand=True)

    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))

    root.mainloop()
