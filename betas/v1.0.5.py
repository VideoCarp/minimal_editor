# Imports
import time
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox as tkmsg
from tkinter import filedialog


# Initialize Window
window = Tk()

window.title("Notepad--")
#window.iconbitmap("icon.ico")

# Set up
window.configure(bg="#222")
window.configure(width = 200, height = 100)
window.tk.call('tk', 'scaling', 3.0) # Fix resolution


# Main
def msgbox(title, desc):
  tkmsg.showinfo(title, desc)

# OpenFile
def openDialog():
  openableTypes = [("All Files", "*"), ("Python Files", "*.py"), ("Text Files", "*.txt")]
  # Types of files, (Name, Extension)
  openedPath = filedialog.askopenfilename(filetypes=openableTypes)
  # The path to the opened file.
  opened = open(openedPath)
  # May be useless, but just to be safe, direct open through variable.
  readOpened = opened.read()
  # Reads Opened file
  opened.close()
  # Close opened file
  text_box.delete(1.0, END)
  # Remove all text
  text_box.insert(1.0, readOpened)
  # Write down into text box.
  msgbox("Opened", "File opened successfully.")

# Run As Python
def _runModule():
  msgbox('Ran as Python', "Successfully ran file.")
  eval(text_box.get(1.0, END))
# Run As Lua
def runLua():
  msgbox("Ran as Lua.", "Successfully ran file.")
  luaGen = open("minimal_luaexec.lua", "+w")
  luaGen.write("-- Minimal Editor created this file" + text_box.get(1.0, END))
  exec(luaGen.read())
  luaGen.close()


# The Input Box
text_box = ScrolledText(background="#222", foreground="#aaa") # Main Text Box


def saveBox():
  files = [('All Files', '*.*'),  
          ('Python Files', '*.py'), 
          ('Text Document', '*.txt')] 
  # Ask Dialog
  file = filedialog.asksaveasfile(filetypes = files, defaultextension = files)
  # Write and Close
  file.write(text_box.get(1.0, END)); file.close()
  # Confirm
  msgbox("Saved", "File has been saved successfully.")

# Menus
_menu = Menu()
fileMenu = Menu(_menu, tearoff=0)
fileMenu.add_command(label="Open", command=openDialog)
fileMenu.add_command(label="Save", command=saveBox)

windowMenu = Menu(_menu, tearoff=0)
windowMenu.add_command(label="Run Script as Python", command=_runModule)
windowMenu.add_command(label="Run Script as Lua", command=runLua)
windowMenu.add_command(label="Quit", command=window.quit())

_menu.add_cascade(label="File", menu=fileMenu)
_menu.add_cascade(label="Window", menu=windowMenu)

# West, East, North, South
window.config(menu=_menu)
text_box.grid(column=1, row=2)
window.mainloop()
