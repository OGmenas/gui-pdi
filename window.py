################################ PRIMERA ITERACIÓN CYMON GUI #########################################

from tkinter import *
from tkinter import Button, Label, ttk
from typing import Text
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import os

root = Tk()




def getimage():
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Selecciona una imagen",filetypes=(("JPG FILE","*.jpg"),("PNG FILE","*.png"),("ALL FILES","(*.*)")))
    img = Image.open(fln)
    img.thumbnail((300,300))
    img = ImageTk.PhotoImage(img)
    img_prev_label.configure(image=img)
    img_prev_label.image=img
    
    return None

frame=Frame(root)
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
frame.grid(row=0, column=0, sticky=N+S+E+W)
grid=Frame(frame)
grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
Grid.rowconfigure(frame, 7, weight=1)
Grid.columnconfigure(frame, 0, weight=1)



img_prev_label =Label(root)
img_prev_label.grid(column=0,row=1)
apply_btn = Button(root,text='>>').grid(column=1,row=3)
img_apply_label = Label(root,padx=100,pady=100).grid(column=2,row=1)

open_btn = Button(root,text='Abrir Imagen',command=getimage).grid(column=0,row=5)
styles_combo= ttk.Combobox(root,state='readonly',values=['cyberpunk','acuarela']).grid(column=1,row=5)
save_btn = Button(root,text='Guardar Imagen').grid(column=2,row=5)


style_text = Text(root)

root.title('Cymon v0.0.1')
root.geometry("1024x768")


root.mainloop()