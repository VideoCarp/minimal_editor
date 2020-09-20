# Imports
import time
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox as tkmsg
from tkinter import filedialog


# Initialize Window
window = Tk()

window.title("Notepad--")
window.iconbitmap("icon.ico")

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


def _runModule():
  msgbox('Output:', eval(text_box.get(1.0, END)))

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


# Buttons
saveButton = Button(background="#222", foreground="#aaa", text="Save", command = saveBox)
openButton = Button(background="#222", foreground="#aaa", text="Open", command = openDialog)
evalButton = Button(background="#222", foreground="#aaa", text="Run Script", command = _runModule)

# West, East, North, South
saveButton.grid(column=1, row=1, sticky=W)
openButton.grid(column=1, row=1, sticky=W, padx=75)
evalButton.grid(column=1, row=1, sticky=W, padx=160)
text_box.grid(column=1, row=2)
window.mainloop()
