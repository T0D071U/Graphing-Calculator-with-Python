# --- imports ---
import tkinter as tk
import plot as pl
from math import *
import mathM as mp
# --- setup ---
root = tk.Tk()
root.title("Graphing Calculator")

# --- functions ---

def calcAnswer():
  number = numInput.get()
  try:
    x = str(eval(number))
    numInput.delete(0, 'end')
    numInput.insert(0, x)
  except:
    numInput.delete(0, 'end')
    numInput.insert(0, "Try something else")

def graphAnswer():
  function = mp.graphList()
  pl.newGraph(function)
  


def quits():
  global tk
  tk.messagebox.showinfo("showinfo", "Information")
# --- tkinter ---
numLabel = tk.Label(root, text="Put Calculation here:", width=20, height=3)
numInput = tk.Entry(root, text="test")
calculateButton = tk.Button(root, text = "Calculate an answer", width=20, height=3, command=calcAnswer)
graphButton = tk.Button(root, text="Graph a function", width=20, height=3, command=graphAnswer)
helpButton = tk.Button(root, text="Help", width=20, height=3, command=help)
exitButton = tk.Button(root, text="Quit", width=20, height=3, command=quits)

numLabel.grid(row=0, column=0)
numInput.grid(row=0, column=1)
calculateButton.grid(row=1, column=1)
graphButton.grid(row=2, column=1)
helpButton.grid(row=1, column=0)
exitButton.grid(row=2, column=0)

# --- functions calls ---




root.mainloop()