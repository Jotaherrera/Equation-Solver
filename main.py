from tkinter import *
from tkinter import ttk


def Main():
    # Config
    root.iconbitmap("./public/images/function.ico")
    root.title("Equation Solver")
    root.geometry("540x510")
    root.resizable(False, False)

    # Equation Entry Frame
    lf = ttk.LabelFrame(root, text="  Ingrese el Polinomio ")
    lf.grid(row=0, column=0, padx=20, pady=10)

    # Equation Entry
    eqEntry = ttk.Entry(lf, font=("Helvetica", 15), width="15")
    eqEntry.grid(row=0, column=0, pady=15, padx=10)

    # Buttons frame
    bf = ttk.LabelFrame(root, text="  Escoja el método ")
    bf.grid(row=1, column=0, padx=0, pady=10)

    # Buttons
    tanteoButton = ttk.Button(
        bf,
        width="22",
        text="Tanteo",
        style="Accent.TButton",
        # command=pass_generator,
    )
    biseccionButton = ttk.Button(
        bf,
        width="22",
        text="Bisección",
        style="Accent.TButton",
        # command=pass_generator,
    )
    reglaFalsaButton = ttk.Button(
        bf,
        width="22",
        text="Regla Falsa",
        style="Accent.TButton",
        # command=pass_generator,
    )

    # Buttons placing
    tanteoButton.grid(row=0, column=0, pady=15, padx=12, ipady=8)
    biseccionButton.grid(row=1, column=0, pady=15, padx=12, ipady=8)
    reglaFalsaButton.grid(row=2, column=0, pady=15, padx=12, ipady=8)

    # Answer and iterations Frame
    af = ttk.LabelFrame(root, text="    Respuesta          Iteraciones    ")
    af.grid(row=2, column=0, padx=20, pady=10)

    # Answer output
    ansOutput = ttk.Entry(af, font=("Helvetica", 15), width="6")
    ansOutput.grid(row=0, column=0, pady=15, padx=15)
    ansOutput.config(state=DISABLED)

    # Iterations Output
    itOutput = ttk.Entry(af, font=("Helvetica", 15), width="6")
    itOutput.grid(row=0, column=1)
    itOutput.config(state=DISABLED)


if __name__ == "__main__":
    root = Tk()

    root.call("source", "./src/Tk Theme/azure.tcl")
    root.call("set_theme", "dark")

    main_app = Main()
    root.mainloop()
