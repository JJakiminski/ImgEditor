import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import PIL
from PIL import Image
from PIL import ImageTk

HEIGHT = 700
WIDTH = 800
global image
global file_path


def get_image():
    global file_path
    file_path = filedialog.askopenfilename()
    show_path['text'] = file_path
    image = Image.open(file_path)
    image.load()
    return file_path


    
def display():
    for widget in lower_frame.winfo_children():
        widget.destroy()
    canvas = tk.Canvas(lower_frame, bg="yellow")
    canvas.pack(expand = 1, fill = tk.BOTH)
    img = Image.open(file_path)
    canvas.image = ImageTk.PhotoImage(img)
    canvas.create_image(0,0, image = canvas.image, anchor = "nw")
    
def blacknwhite():
    for widget in lower_frame.winfo_children():
        widget.destroy()
    canvas = tk.Canvas(lower_frame, bg="yellow")
    canvas.pack(expand = 1, fill = tk.BOTH)
    img = Image.open(file_path)
    bnw = img.convert('L')
    canvas.image = ImageTk.PhotoImage(bnw)
    canvas.create_image(0,0, image = canvas.image, anchor = "nw")

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

show_path = tk.Label(frame)
show_path.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text='Wybierz zdjęcie', command = lambda: get_image())
button.place(relx=0.7, relheight=1, relwidth=0.1)

button = tk.Button(frame, text='Załaduj', command = lambda: display())
button.place(relx=0.8, relheight=1, relwidth=0.1)

button = tk.Button(frame, text="Czarno", command = lambda: blacknwhite())
button.place(relx=0.9, relheight=1, relwidth=0.1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


root.mainloop()
