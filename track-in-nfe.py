import getpass
import platform
import os
from tkinter import *
from tkinter import filedialog, Button
from pdf2image import convert_from_path
from PIL import Image
from datetime import datetime

def getFileNfe():
    selectFileNfe = filedialog.askopenfilename(initialdir = "/home/bdos/Desktop",title = "Selecione a NFe",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
    imageNfe = convert_from_path(selectFileNfe, 500)
    for nfe in imageNfe:
        nfe.save('tempNfe.jpg', 'JPEG')

def getFileTrack():
    selectFileTrack = filedialog.askopenfilename(initialdir = "/home/bdos/Desktop",title = "Selecione a NFe",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
    imageTrack = convert_from_path(selectFileTrack, 500)
    for track in imageTrack:
        track.save('tempTrack.jpg', 'JPEG')

def start():
    imageTrack = Image.open(r'tempTrack.jpg')
    imageNfe = Image.open(r'tempNfe.jpg')

    top, left, right, bottom = 126, 0 , 2073, 1011
    newImage = imageTrack.crop((left, top, right, bottom))
    imageNfe.paste(newImage, (136, 3680))
    
    user = getpass.getuser()

    now = datetime.now()
    sys = platform.system()
    if (sys == 'Linux'):
        imageNfe.save(r'/home/{}/Desktop/Nota_{}-{}-{}_{}-{}-{}.pdf'.format(user, now.day, now.month, now.year, now.hour, now.minute, now.second))
    else:
        imageNfe.save(r'C:\\Users\\\{}\\Desktop\\Nota_{}-{}-{}_{}-{}-{}.pdf'.format(user, now.day, now.month, now.year, now.hour, now.minute, now.second))

    os.remove('tempTrack.jpg')
    os.remove('tempNfe.jpg')

windows = Tk()
windows.title("Adicionar código de rastreio em NFe")
windows.geometry('560x400')
windows.resizable(False, False)

frame1 = Frame(windows, width = 280, height = 260, bg = 'white').grid(row = 0, column=0)
buttonNFe = Button(frame1, text="Selecionar NFe", height = 4, width = 20, command = getFileNfe).grid(row = 0, column = 0)
label1 = Label(frame1, text='Selecione a NFe', padx=30, pady=50).place(x = 30, y = 200, width = 230, height = 25)

frame2 = Frame(windows, width = 280, height = 260, bg = 'white').grid(row = 0, column=1)
buttonTrack = Button(frame2, text="Selecionar Rastreio", height = 4, width = 20, command = getFileTrack).grid(row = 0, column = 1)
label2 = Label(frame2, text='Selecione o arquivo de rastreio', padx=30, pady=50).place(x = 310, y = 200, width = 230, height = 25)

frame3 = Frame(windows, width = 560, height = 170, bg = 'white').grid(row = 1, column=0, columnspan = 2)
ButtonStart = Button(frame3, text="Mesclar", height = 3, width = 40, command = start).grid(row = 1, column = 0, columnspan = 2)

windows.mainloop()
