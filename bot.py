
from tkinter import messagebox
from tkinter.font import NORMAL
from pyautogui import *
import pyautogui as pg
from time import sleep
import pywhatkit as kt
import keyboard as k
import tkinter as tk
from tkinter import DISABLED, END, W, BooleanVar, Button, Checkbutton, Entry, Label, PhotoImage, Place, StringVar, Tk, filedialog, Text
import threading


#script

#numero de telefone
def phone_no():
    global telefone
    telefone = vtelefone.get()
    print(telefone)

#manda mensagem wpp
def sendMensage():
    kt.sendwhatmsg_instantly(str(telefone),"Achei Partida!") 
    time.sleep(1)
    width, height = pg.size()
    pg.click(width / 2, height / 2)
    pg.press('enter')

#mouse click
def click(x, y):
    pg.moveTo(x, y)
    pg.click()


#procura imagem na tela
def check_screen():
    button_pos_small = pg.locateOnScreen("images/button0.png", confidence=0.8)
    button_pos_medium = pg.locateOnScreen("images/button1.png", confidence=0.8)
    button_pos_large = pg.locateOnScreen("images/button2.png", confidence=0.8)
    button_pos_xlarge = pg.locateOnScreen("images/button3.png", confidence=0.8)
            
    if button_pos_small != None:
        click(button_pos_small.left, button_pos_small.top)
        return True

    if button_pos_medium != None:
        click(button_pos_medium.left, button_pos_medium.top)

        return True

    if button_pos_large != None:
        click(button_pos_large.left, button_pos_large.top)

        return True

    if button_pos_xlarge != None:
        click(button_pos_xlarge.left, button_pos_xlarge.top)

        return True

    return False

#procurndo fila

def botaoFila():
    threading.Thread(target=fila).start() 

def fila():
    messagebox.showinfo("Bot Fila","Procurando Fila")
   
    while True:
        print("procurando fila...")

        #Procura e manda mensagem
        if (vmensagem.get()) and check_screen():
            sendMensage()

        #Não manda mensagem   
        else:
            check_screen()
        #Para de procurar 
        if vParaFila == 1:
            messagebox.showinfo("Bot Fila","Fila Parada!")
            resetStop()
            break

       
  
#Para de Procurar fila

vParaFila= 0

def stop():
    global vParaFila
    vParaFila= 1

def resetStop():
    global vParaFila
    vParaFila=0

#Placeholder
def placeholder(event):
    vtelefone.config(state=NORMAL)
    vtelefone.delete(0, END)
    

#inteface
root = tk.Tk()
root.title("Bot Fila")
root.configure(background="black")
root.iconbitmap(r"icon.ico")
root.resizable(width=False, height=False)
canvas = tk.Canvas(root, height=300, width=700, bg="black")

global background_images
background_images = [
        PhotoImage(file="bgOff.png"),
        PhotoImage(file="bgOn.png"),
]


#background
bg= background_images[1]
bg_Image=Label(root, image=bg)
bg_Image.place(x=0,y=0, relwidth=1,relheight=1)
canvas.pack()



#variaveis
vmensagem=BooleanVar()
vtelefone=Entry(root)

#placeholder
vtelefone.insert(0,"+5500123456789")
vtelefone.config(state=DISABLED)
vtelefone.bind("<Button-1>",placeholder)
vtelefone.pack()

#Numero Imput
vtelefone.place(x=20,y=100,width=300, height=50)
salvar=Button(root,text="Salvar",background="#263D42",fg="white", command=phone_no).place(x=20, y=230, width= 100, height=40)

#receber mensagem Checkbox
cb_mensagem=Checkbutton(root,text="Desejo receber a mensagem",takefocus=0,variable=vmensagem,onvalue= True,offvalue= False)
cb_mensagem.place(x=20, y=170, width=300, height=40)


#RunApp Button
runApp = tk.Button(root, text="Procurar Fila",padx=10, pady=10, fg="white", bg="#263D42", command=botaoFila)

#Stop Button
exit=Button(root, text="Stop", padx=70, pady=10, fg="white", bg="#263D42",command=stop).place(x=615, y=275, width=80, height=80 )

runApp.pack()

root.mainloop()
