from tkinter import *


class GUI:
    def __init__(self, size="400x500", height=500, width=400):
        self.root = Tk()
        self.root.title("E-Okul Not Dağılımı")
        self.root.geometry(size)
        self.root.resizable(False, False)

        self.main_frame = Frame(self.root, background="skyblue")
        self.main_frame.place(height=height, width=width)

        self.first_page()

    def run(self):
        self.root.mainloop()

    def first_page(self):
        text_frame = Frame(self.main_frame, background="skyblue")
        text_frame.place(x=100, y=100, height=150, width=200)

        okul_tf = TextField(text_frame, text="Okul Adı", y=0)
        mudur_tf = TextField(
            text_frame, text="Müdür Adı", y=50)
        ogretmen_tf = TextField(
            text_frame, text="Öğretmen Adı", y=100)


class TextField(Frame):
    def __init__(self, root, text, padx=5, pady=5, background="skyblue", fontVar=("Arial", "10"), fg="black", bg="white", heigth=20, width=200, x=0, y=0):
        super().__init__(root)
        self.frame = Frame(root, background=background)
        self.frame.place(x=x, y=y, height=heigth, width=width)

        self.label = Label(self.frame, text=text, padx=padx,
                           pady=pady, font=fontVar, fg=fg, bg=background, anchor="w")
        self.label.place(x=0, width=100, height=20)

        self.entry = Entry(self.frame)
        self.entry.place(x=100, width=100, height=20)
