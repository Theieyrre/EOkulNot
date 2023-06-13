from tkinter import *
from data_table import DataTable


class GUI:
    # TODO add openpyxl and excel funtionality
    # TODO add if possible pdf output
    # TODO add destination dropdown list
    # TODO add helper class for functionality (maybe)
    def __init__(self, size="300x500", height=500, width=300):
        self.root = Tk()
        self.root.title("E-Okul Not Dağılımı")
        self.root.geometry(size)
        self.root.resizable(False, False)

        self.dt = DataTable()

        self.main_frame = Frame(self.root, background="skyblue")
        self.main_frame.place(height=height, width=width)

        self.eokul_component = EOkulComponent(self.main_frame)

        self.names_component = NamesComponent(self.main_frame)

    def run(self):
        # TODO seperate to a component
        # TODO add check buttons for different file formats (if possible)

        button = Button(self.main_frame, text="Oluştur", command=self.create_files)
        button.place(x=55, y=280, height=25, width=195)

        self.root.mainloop()

    def create_files(self):
        data = self.eokul_component.get_data()
        self.dt.insert_data(data)


class EOkulComponent:
    def __init__(self, root, x=50, y=150, height1=150, height2=30, width=200):
        eokul_frame = Frame(root, background="skyblue")
        eokul_frame.place(x=x, y=y, height=height1, width=width)

        eokul_label = Label(
            eokul_frame,
            text="E-Okuldan kopyalanan tabloyu aşağıdaki alana yapıştırınız",
            font="arial 10",
            anchor="w",
            padx=5,
            pady=5,
            wraplength=width,
            justify="left",
            bg="skyblue",
        )
        eokul_label.place(x=0, y=0, height=height2 * 2, width=width)

        eokul_desc_label = Label(
            eokul_frame,
            text="İlk öğrenci numarasından seçip tabloyu kopyalayınız",
            font="arial 8",
            anchor="w",
            padx=5,
            wraplength=width,
            justify="left",
            bg="skyblue",
        )
        eokul_desc_label.place(x=0, y=height2 * 2, height=height2, width=width)

        self.eokul_veri = Entry(eokul_frame)
        self.eokul_veri.place(x=5, y=height2 * 3, height=height2, width=width)

    def get_data(self):
        return self.eokul_veri.get()


class NamesComponent:
    def __init__(self, root, dist_x=50, dist_y=30, height=120, width=200):
        self.text_frame = Frame(root, background="skyblue")
        self.text_frame.place(x=dist_x, y=dist_y, height=height, width=width)

        self.okul_tf = TextField(self.text_frame, text="Okul Adı", y=dist_y * 0)
        self.mudur_tf = TextField(self.text_frame, text="Müdür Adı", y=dist_y * 1)
        self.ogretmen_tf = TextField(self.text_frame, text="Öğretmen Adı", y=dist_y * 2)
        self.sube_tf = TextField(self.text_frame, text="Şube", y=dist_y * 3)

    def get_data(self):
        return [self.get_okul(), self.get_mudur(), self.get_ogretmen(), self.get_sube()]

    def get_okul(self):
        return self.okul_tf.get()

    def get_mudur(self):
        return self.mudur_tf.get()

    def get_ogretmen(self):
        return self.ogretmen_tf.get()

    def get_sube(self):
        return self.sube_tf.get()


class TextField(Frame):
    def __init__(
        self,
        root,
        text,
        padx=5,
        pady=5,
        background="skyblue",
        fontVar=("Arial", "10"),
        fg="black",
        bg="white",
        heigth=20,
        width=200,
        x=0,
        y=0,
    ):
        super().__init__(root)
        self.frame = Frame(root, background=background)
        self.frame.place(x=x, y=y, height=heigth, width=width)

        self.label = Label(
            self.frame,
            text=text,
            padx=padx,
            pady=pady,
            font=fontVar,
            fg=fg,
            bg=background,
            anchor="w",
        )
        self.label.place(x=0, width=100, height=20)

        self.entry = Entry(self.frame)
        self.entry.place(x=100, width=100, height=20)

    def get(self):
        return self.entry.get()
