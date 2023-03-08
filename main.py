from tkinter import *


def Main():
    # Config
    root.iconbitmap("./public/images/function.ico")
    root.title("Equation Solver")
    root.geometry("500x500")
    root.resizable(False, False)


if __name__ == "__main__":
    root = Tk()

    root.call("source", "./src/Tk Theme/azure.tcl")
    root.call("set_theme", "dark")

    main_app = Main()
    root.mainloop()
