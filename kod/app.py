from tkinter import *
from tkinter import messagebox
from data_table import DataTable
from workbook import ExcelWriter
import os


class App:
    # TODO seperate generate button pdf and excel
    # TODO update width to better view long names
    def __init__(self, size="300x500", height=500, width=300):
        self.root = Tk()
        self.root.eval("tk::PlaceWindow . center")
        self.root.title("E-Okul Not Dağılımı")
        self.root.geometry(size)
        self.root.resizable(False, False)

        self.main_frame = Frame(self.root, background="skyblue")
        self.main_frame.place(height=height, width=width)

        self.eokul_component = EOkulComponent(self.main_frame)

        self.names_component = NamesComponent(self.main_frame)

        button = Button(self.main_frame, text="Oluştur", command=self.create_files)
        button.place(x=55, y=370, height=25, width=195)

    def run(self):
        self.root.mainloop()

    def create_files(self):
        self.names = self.names_component.get_data()
        data = self.eokul_component.get_data()
        self.dt = DataTable(data)
        proje_columns = self.read_criterias("./veri/proje_kriterler.txt")
        dersici_columns = self.read_criterias("./veri/dersici_kriterler.txt")

        sinif = self.names_component.get_sube()

        self.create_file("1.Proje", proje_columns, sinif + " 1.Proje.xlsx")
        self.create_file(
            "1.Ders Et.Kat", dersici_columns, sinif + " 1. Ders Et.Kat.xlsx"
        )
        self.create_file(
            "2.Ders Et.Kat", dersici_columns, sinif + " 2. Ders Et.Kat.xlsx"
        )
        self.create_file(
            "3.Ders Et.Kat", dersici_columns, sinif + " 3. Ders Et.Kat.xlsx"
        )

        messagebox.showinfo(
            "E-Okul Not Dağılımı", "Dosyalar başarıyla Masaüstünde oluşturuldu"
        )

    def create_file(self, col, columns, filename):
        desktop = os.path.expanduser("~/Desktop")
        filename = os.path.join(desktop, filename)
        temp = self.dt.fill_sub_df(col, columns)
        ew = ExcelWriter(col, columns, self.names)
        ew.add_dataframe(temp)
        ew.add_names(self.names[2], self.names[1], self.names[4])
        ew.save(filename)

    def read_criterias(self, filename) -> list:
        grade_columns = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                grade_columns.append(line.replace("\n", ""))

        return grade_columns


class EOkulComponent:
    def __init__(self, root, x=50, y=240, height1=150, height2=30, width=200):
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
    def __init__(self, root, dist_x=50, dist_y=30, height=210, width=200):
        self.text_frame = Frame(root, background="skyblue")
        self.text_frame.place(x=dist_x, y=dist_y, height=height, width=width)

        self.okul_tf = TextField(self.text_frame, text="Okul Adı", y=dist_y * 0)
        self.mudur_tf = TextField(self.text_frame, text="Müdür Adı", y=dist_y * 1)
        self.ogretmen_tf = TextField(self.text_frame, text="Öğretmen Adı", y=dist_y * 2)
        self.sube_tf = TextField(self.text_frame, text="Şube", y=dist_y * 3)
        self.ders_tf = TextField(self.text_frame, text="Ders", y=dist_y * 4)
        self.yil_tf = TextField(self.text_frame, text="Eğitim Yılı", y=dist_y * 5)
        self.donem_tf = TextField(self.text_frame, text="Dönem", y=dist_y * 6)

    def get_data(self):
        return [
            self.get_okul(),
            self.get_mudur(),
            self.get_ogretmen(),
            self.get_sube(),
            self.get_ders(),
            self.get_yil(),
            self.get_donem(),
        ]

    def get_okul(self):
        return self.okul_tf.get().upper()

    def get_mudur(self):
        return self.mudur_tf.get().upper()

    def get_ogretmen(self):
        return self.ogretmen_tf.get().upper()

    def get_sube(self):
        return self.sube_tf.get().upper()

    def get_ders(self):
        return self.ders_tf.get().upper()

    def get_yil(self):
        return self.yil_tf.get().upper()

    def get_donem(self):
        return self.donem_tf.get().upper()


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
        textval="",
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

        self.entry = Entry(self.frame, textvariable=textval)
        self.entry.place(x=100, width=100, height=20)

    def get(self):
        return self.entry.get()
