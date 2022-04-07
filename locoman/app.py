from fileinput import filename
import tkinter as tk
from tkinter.filedialog import askopenfilename
from views import *

window=tk.Tk()
window.title(" Locoman Desktop App ")
window.geometry("600x400")

newlabel = tk.Label(text = " locomanistired.io , Remember the name ")
newlabel.grid(column=0,row=0)

filename = askopenfilename()
my_document = open(filename, "rb")
document = docx.Document(my_document)

#readFiles =readingDocuments(filename)
print(filename)
print(document)

window.mainloop()