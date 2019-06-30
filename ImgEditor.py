import tkinter as tk

HEIGHT = 700
WIDTH = 800


def test_function(entry):
    print("This is the entr: ", entry)

def test_function2():
    file_path = filedialog.askopenfilename()
    return file_path

root = tk. Tk()

canvas = tk.Canvas(root, height=HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text='Test button', command = lambda: test_function2())
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, text="This is a label", bg="yellow")
label.place(relwidth=1, relheight=1)

root.mainloop()






#root.withdraw()
#file_path = filedialog.askopenfilename()
#print(file_path)
