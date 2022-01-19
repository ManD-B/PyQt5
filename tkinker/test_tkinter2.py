# imports
import tkinter
import tkinter.scrolledtext as tkst
from tkinter import Menu
from tkinter import ttk


# Click OK button
def clickOK():
    text = "Your gender is " + gender.get()
    text = text + "\nYou are " + str(age.get()) + " years old.\n"
    scrt.insert(tkinter.INSERT, text)                    # insert text in a scrolledtext
    scrt.see(tkinter.END)


# Click a exit menu
def clickExit():
    win.quit()
    win.destroy()
    exit()


if __name__ == '__main__':
    win = tkinter.Tk()                                   # Create instance
    win.title("tkinter sample")                     # Add a title

    labelName = ttk.Label(win, text="Name:")          # Create a label
    labelName.grid(column=0, row=0)                  # Label's grid

    labelAge = ttk.Label(win, text="Age:")          # Create a label
    labelAge.grid(column=0, row=1)                  # Label's grid

    labelGender = ttk.Label(win, text="Gender:")    # Create a label
    labelGender.grid(column=0, row=2)               # Label's grid

    labelGender = ttk.Label(win, text="More Infomation:")    # Create a label
    labelGender.grid(column=0, row=3)               # Label's grid

    name = tkinter.IntVar()                                       # Integer variable
    nameEntered = ttk.Entry(win, width=15, textvariable=name)  # Create a textbox
    nameEntered.grid(column=1, row=0)

    age = tkinter.IntVar()                                       # Integer variable
    ageEntered = ttk.Entry(win, width=15, textvariable=age)  # Create a textbox
    ageEntered.grid(column=1, row=1)

    gender = tkinter.StringVar()                                         # String variable
    genderCombo = ttk.Combobox(win, width=7, textvariable=gender)   # Create a combobox
    genderCombo['values'] = ("Female", "Male")                      # Combobox's items
    genderCombo.grid(column=1, row=2)
    genderCombo.current(0)

    scrt = tkst.ScrolledText(win, width=33, height=3, wrap=tkinter.WORD) # Create a scrolledtext
    scrt.grid(column=0, row=4, columnspan=3)
    scrt.focus_set()                                                # Default focus

    action = ttk.Button(win, text="OK", command=clickOK)    # Create a button
    action.grid(column=1, row=5)

    menuBar = Menu(win)                                     # Create a menu
    win.config(menu=menuBar)

    fileMenu = Menu(menuBar, tearoff=0)                     # Create the File Menu
    fileMenu.add_command(label="New")                       # Add the "New" menu
    fileMenu.add_separator()                                # Add a separator
    fileMenu.add_command(label="Exit", command=clickExit)   # Add the "Exit" menu and bind a function
    menuBar.add_cascade(label="File", menu=fileMenu)

    win.resizable(0, 0)             # Disable resizing the GUI
    win.mainloop()                  # Start GUI