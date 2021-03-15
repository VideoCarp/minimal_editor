# Imports
import time; import webbrowser; import subprocess
from tkinter import *; import os
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox as tkmsg
from tkinter import filedialog



# Manage window
window = Tk()

window.title("Notepad--")
#window.iconbitmap("icon.ico")
window.configure(bg="#222")
window.configure(width = 200, height = 100)
window.tk.call('tk', 'scaling', 3.0) # Fix resolution


# Main

# main.funcs
def msgbox(title, desc):
  tkmsg.showinfo(title, desc)

def saveBox():
  files = [('All Files', '*.*'),  
          ('Python Files', '*.py'), 
          ('Text Document', '*.txt')] 
  
  file = filedialog.asksaveasfile(filetypes = files, defaultextension = files)
  file.write(text_box.get(1.0, END)); file.close()
  msgbox("Saved", "File has been saved successfully.")


def openDialog():
  openableTypes = [("All Files", "*"), ("Python Files", "*.py"), ("Text Files", "*.txt")]
  openedPath = filedialog.askopenfilename(filetypes=openableTypes)
  opened = open(openedPath)
  readOpened = opened.read()
  opened.close()
  text_box.delete(1.0, END)
  text_box.insert(1.0, readOpened)
  msgbox("Opened", "File opened successfully.")


def _runModule():
  msgbox('Ran as Python', "Successfully ran file.")
  eval(text_box.get(1.0, END))



def runLua():
  msgbox("Ran as Lua.", "Successfully ran file.")
  luaGen = open("minimal_luaexec.lua", "+w")
  luaGen.write("-- Minimal Editor created this file" + text_box.get(1.0, END))
  subprocess.check_output(['lua', '-l', 'demo', '-', 'minimal_luaexec.lua'])
  luaGen.close()


def html_page():
  msgbox("HTML", "Ran HTML file successfully.")
  min_html = open("minimal_html.html", "+w")
  min_html.write("<!-- minimal_editor -->\n" + text_box.get(1.0, END))
  min_html.close()
  webbrowser.open(f"file://{os.path.realpath('minimal_html.html')}")


def js_page():
  msgbox("JavaScript", "Ran JavaScript as webpage successfully. Node.js is currently unsupported, manually run.")
  min_js = open("minimal_js.html", "+w")
  min_js.write(f"<script>{text_box.get(1.0, END)}</script>")
  min_js.close()
  webbrowser.open(f"file://{os.path.realpath('minimal_js.html')}")


def bashRun():
  msgbox("Run Batch", "Batch file ran successfully.")
  file_batch = open("minimal_editor.bat", "+w")
  file_batch.write(text_box.get(1.0, END))
  file_batch.close()
  subprocess.call(os.path.realpath("minimal_editor.bat"))



def warnclose():
  if tkmsg.askyesno("Quit", "Save and Exit?"):
    saveBox()
    window.destroy()
  else:
    window.destroy()

window.protocol("WM_DELETE_WINDOW", warnclose)

def saveBox():
  files = [('All Files', '*.*'),  
          ('Python Files', '*.py'), 
          ('Text Document', '*.txt')] 
  
  file = filedialog.asksaveasfile(filetypes = files, defaultextension = files)
  file.write(text_box.get(1.0, END)); file.close()
  msgbox("Saved", "File has been saved successfully.")

def saveHotkey(event): # Event argument neededin order for func to work.
  print("Save hotkey pressed")
  saveBox()

# Main.widgets
text_box = ScrolledText(background="#222", foreground="#aaa")
# Menus
_menu = Menu()
fileMenu = Menu(_menu, tearoff=0)
fileMenu.add_command(label="Open", command=openDialog)
fileMenu.add_command(label="Save", command=saveBox)

runMenu = Menu(_menu, tearoff=0)
runMenu.add_command(label="Run Script as Python", command=_runModule)
runMenu.add_command(label="Run Script as Lua", command=runLua)
runMenu.add_command(label="Run File as Webpage (HTML)", command=html_page)
runMenu.add_command(label="Run as JavaScript Page", command=js_page)
runMenu.add_command(label="Run as Batch", command=bashRun)


_menu.add_cascade(label="File", menu=fileMenu)
_menu.add_cascade(label="Run", menu=runMenu)

# Detects keypress. Check this stackoverflow answer if you want to use other key presses: https://stackoverflow.com/a/16082411
window.bind("<Control-s>", saveHotkey)

# West, East, North, South (sticky=) options
window.config(menu=_menu)
text_box.grid(column=1, row=2)
window.mainloop()
