from tkinter import *
import os
from tkinter import filedialog as fd

global folder_selected

def openProj():
    global folder_selected 
    folder_selected = fd.askdirectory()
    
    FileZ.destroy()
 
FileZ =Tk()
FileZ.resizable(False,False)
FileZ.title("Open Or Create A Project")
FileZ.geometry("600x620")
#FileZ.wm_attributes('-toolwindow', True)

Button(FileZ, text="OPEN A PROJECT", font=('Times', 15, 'normal'), width=52,
bg='gray', fg='white', command=openProj).grid(row=0, column=0, padx=10, pady=10)


Label(FileZ, text="INFORMATION:",font=('Times', 10, 'normal')).grid(row=2, column=0, padx=10, pady=10)

Inf = Text(FileZ, font=('Times', 10, 'normal'), width=95)
Inf.grid(row=3, column=0, padx=10, pady=10)
Inf.insert(INSERT,
"""Dear Beloved User, 
A warm welcoming love from Piva,
Before you start, please make sure that you have Python installed.

Use 'Open A Project' open an existing project.

NOTE Projects Are Just Folders

Thank you, 
With LOVE,
Piva Team...
""")
Inf.config(state=DISABLED)
FileZ.mainloop()

def openF():
    fn = lbox.curselection()[0]
    FN = lbox.get(fn)
    orig_File = folder_selected+"/"+FN
    file = open(orig_File, 'r')
    CodE = file.read()
    CODE_area.delete(1.0, END)
    CODE_area.insert(INSERT, CodE)
    Editor.title("Piva-"+ FN)

def runner():
    fn = lbox.curselection()[0]
    FN = lbox.get(fn)
    orig_File = folder_selected+"/"+FN
    try:
        os.system(f"python {orig_File}")
    except:
       os.system(f"python3 {orig_File}") 

def saver():
    endCode = CODE_area.get(1.0, END)
    fn = lbox.curselection()[0]
    FN = lbox.get(fn)
    orig_File = folder_selected+"/"+FN
    if orig_File != '':
        file = open(orig_File, 'w')
        file.write(endCode)
        file.close()
    if orig_File == "":
        file = open(orig_File, 'w')
        file.write(endCode)
        file.close()

def new():
    New = Tk()
    New.title("New File")
    #New.wm_attributes('-toolwindow', True)
    def creator():
        name = NME.get()
        file = open(folder_selected+"/"+name, 'w')
        file.write("")
        file.close()
    Label(New, text="File Name").grid(row=0,column=0)
    NME = Entry(New)
    NME.grid(row=0,column=1)
    Button(New, text="Create", command=creator).grid(row=1,column=1)
    Label(New, text="NOTE: You May NEED to RESTART the app").grid(row=2,column=1)
    New.mainloop()

def clean():
    print("\033[H\033[J")
    

Editor =Tk()
Editor.title('Piva')
Editor.geometry("900x900")
try:
    flist = os.listdir(folder_selected)
except:
    folder_selected = fd.askdirectory()
    print("Please select a folder")
    flist = os.listdir(folder_selected)

sideBar = Canvas(Editor)
sideBar.pack(side=LEFT, fill=X)
Label(sideBar, text="Python Files").pack()
lbox = Listbox(sideBar, font=('Times', 15, 'normal'))
lbox.pack()
Button(sideBar, text="Open", command=openF).pack(fill=X)
Button(sideBar, text="Save As", command=saver).pack(fill=X)
Button(sideBar, text="Run", command=runner).pack(fill=X)
Button(sideBar, text="Save", command=saver).pack(fill=X)
Button(sideBar, text="New File", command=new).pack(fill=X)
Button(sideBar, text="Clear Terminal", command=clean).pack(fill=X)
 
# THE ITEMS INSERTED WITH A LOOP
for item in flist:
    if '.py' in item:
        lbox.insert(END, item)

mainBar = Canvas(Editor)
mainBar.pack(side=RIGHT, fill=X)
CODE_area = Text(mainBar, width=1000, height=1000)
CODE_area.pack(side= RIGHT, fill=BOTH)
Editor.mainloop()
