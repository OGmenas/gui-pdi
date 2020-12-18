################################# SEGUNDA ITERACION CYMON ######################################


from pathlib import Path
from sys import path
from tkinter import *
import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import os
import cv2
import shutil

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

       #STACK DE FRAMES 
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        #
        for F in (StartPage, PageOne):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


#pagina principal

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        global image_prev_label
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="CYMON", font=controller.title_font)
        

        button1 = tk.Button(self, text="ajustar foto",
                            command=lambda: controller.show_frame("PageOne"))
        
        label.pack(side="top", fill="x", pady=10)

        


        button1.pack()

    

        
#pagina de ajuste

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="ajustando la foto", font=controller.title_font)
        label.pack(side="top", fill="y", pady=10)
        #image_label.pack(fill="x")
        button = tk.Button(self, text="volver atras",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


def getimage(label):
    global temp_img,path, size
    path = filedialog.askopenfilename(initialdir='C:/Users/og/Pictures', title="Selecciona una imagen",filetypes=(("JPG FILE","*.jpg"),("PNG FILE","*.png"),("ALL FILES","(*.*)")))
    img = Image.open(path)
    res = img.size
    print(res)
    temp_img = img 

    img.thumbnail((400,400))
    img = ImageTk.PhotoImage(img)
    size = (img.width(),img.height())
    label.configure(image=img)
    label.image=img

    
    return None

def putimage(label):
    global temp_img
    try:
        img = ImageTk.PhotoImage(temp_img)
        label.configure(image=img)
        label.image=img
        return None
    except expression as identifier:
        return identifier

def get_roi():
    global path,img_adjust_label,pixlist,size
    if(pixlist.index(pixlist[-1])>2):
        pixlist=[pixlist[-2],pixlist[-1]]
    rectimg=cv2.imread(path)
    rectimg = cv2.resize(rectimg,size,interpolation = cv2.INTER_AREA)
    pixel1= pixlist[0]
    pixel2= pixlist[1]
    rectimg = cv2.cvtColor(rectimg,cv2.COLOR_BGR2RGB)
    cv2.rectangle(rectimg,pixel1,pixel2,(0,0,0),3)
    
    
    img = Image.fromarray(rectimg)
    img.thumbnail((800,800))
    rectimg = ImageTk.PhotoImage(img)
    
    img_adjust_label.configure(image=rectimg)
    img_adjust_label.image = rectimg
    
def click_callback(event):
    global pixlist
    print(event)
    point=(event.x, event.y)
    pixlist.append(point)
    print(pixlist, " lista")

def saveimage(img,nombre,path):
    path=os.path.join(path, str(nombre+".jpg"))
    img.save(path)
    
    return None

def applystyle(style):
    global initdir,sampledir,temp_img,img_apply_label
    if (style == None):
        pass #alert
    shutil.rmtree(initdir)
    shutil.rmtree(sampledir)
    os.mkdir(initdir)
    os.mkdir(sampledir)
    saveimage(temp_img,"temporal",initdir)
    os.system("python ./modules/cycleGAN/process_img.py")

    foto= Image.open(sampledir+"/B-num-0epoch-0.png")
    foto.thumbnail((400,400))
    foto = ImageTk.PhotoImage(foto)
    img_apply_label.configure(image=foto)
    img_apply_label.image=foto


    

if __name__ == "__main__":
    #init
    app = SampleApp()
    app.geometry("1024x768")

    #referencia a los objetos pagina
    cursor = app.frames["StartPage"]
    cursor2 = app.frames["PageOne"]

    #imagenes 
    #imagen original
    temp_img= 0
    pixlist = []
    rectimg=0
    path = ''
    size=0
    initdir='./modules/cycleGAN/input_imgs/1/'
    sampledir='./modules/cycleGAN/samples/'
    #frames de fotos


    image_prev_label=Label(cursor,text="aca va la imagen",padx=100,pady=100, ) #imagen original
    img_apply_label = Label(cursor,text="aca va la imagen con efecto",padx=100,pady=100, ) #imagen filtro aplicado
    img_adjust_label = Label(cursor2,text="aca va la imagen",padx=100,pady=100, ) #imagen recortada

    img_adjust_label.bind('<Button-1>',click_callback)

    #botones

    open_btn = Button(cursor,text='Abrir Imagen',command= lambda label =image_prev_label : getimage(label))#carga imagen
    apply_btn = Button(cursor,text='>>',command=lambda style = "aaa":applystyle(style))#aplicar filtro, falta implementar
    styles_combo= ttk.Combobox(cursor,state='readonly',values=['cyberpunk'])#seleccion de filtro, falta implementar
    save_btn = Button(cursor,text='Guardar Imagen')#guardar foto, falta implementar

    open_btn.pack(side="bottom")
    apply_btn.pack(side="bottom")
    save_btn.pack(side="bottom")
    styles_combo.pack(side="bottom")


    get_btn=Button(cursor2,text='refrescar',command= lambda label =img_adjust_label : putimage(label))#trae imagen del frame startpage
    adjust_btm= Button(cursor2,text='ajustar imagen',command= get_roi)#lambda img = temp_img: get_roi(img))#ajusta la aplicacion del filtro, falta implementar
   
    #ubicaciones de los elementos 
    image_prev_label.pack(side="left",fill="both",expand=True)
    img_apply_label.pack(side="right",fill="both",expand=True)

    get_btn.pack()
    adjust_btm.pack()
    img_adjust_label.pack(side=BOTTOM,expand=1)
    app.mainloop()
  
