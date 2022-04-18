from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *

hunians = []
hunians.append(Apartemen("Saul Goodman", 20, 3, 3))
hunians.append(Rumah("Gustavo Fring", 48, 5, 2))
hunians.append(Indekos("Chuck McGill", "Howard Hamlin", 9))
hunians.append(Rumah("Mike Ehrmantraut", 35, 1, 4))

root = Tk()
root.title("Praktikum DPBO Python")

def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary = Label(d_frame, text="Summary: " + hunians[index].get_summary(), anchor="w").grid(row=0, column=0, sticky="w")
    
    opts = LabelFrame(top, padx=10, pady=10)
    opts.pack(padx=10, pady=10)
    
    b_exit = Button(opts, text="Exit", command=root.quit)
    b_exit.grid(row=0, column=0)

def document(index):
    top = Toplevel()
    top.title("Dokumen " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary = Label(d_frame, text=hunians[index].get_dokumen(), anchor="w").grid(row=0, column=0, sticky="w")
    
    opts = LabelFrame(top, padx=10, pady=10)
    opts.pack(padx=10, pady=10)
    
    b_exit = Button(opts, text="Exit", command=root.quit)
    b_exit.grid(row=0, column=0)

frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
frame.pack(padx=10, pady=10)

opts = LabelFrame(root, padx=10, pady=10)
opts.pack(padx=10, pady=10)

b_add = Button(opts, text="Add Data", state="disabled")
b_add.grid(row=0, column=0)

b_exit = Button(opts, text="Exit", command=root.quit)
b_exit.grid(row=0, column=1)

# Title Table
idx = Label(frame, text="No", width=5, borderwidth=1, relief="solid")
idx.grid(row=0, column=0)

type = Label(frame, text="Type", width=15, borderwidth=1, relief="solid")
type.grid(row=0, column=1)

owner = Label(frame, text="Owner", width=40, borderwidth=1, relief="solid")
owner.grid(row=0, column=2)

# Isi Table
for index, h in enumerate(hunians):
    idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
    idx.grid(row=index+1, column=0)

    type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
    type.grid(row=index+1, column=1)

    name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
    name.grid(row=index+1, column=2)

    b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
    b_detail.grid(row=index+1, column=3)

    b_dokumen = Button(frame, text="Dokumen ", command=lambda index=index: document(index))
    b_dokumen.grid(row=index+1, column=4)

root.mainloop()
