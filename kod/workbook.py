from openpyxl import Workbook
from openpyxl.styles.alignment import Alignment
import pandas as pd


class ExcelWriter:
    # TODO add borders
    # TODO add grade specific columns
    def __init__(self, col, columns, metadata):
        self.wb = Workbook()
        self.ws = self.wb.active

        size = len(columns)

        # Yıl Okul row
        self.ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=size + 3)

        # Ders Not tipi row
        self.ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=size + 3)

        # Sınıf label
        self.ws.merge_cells(start_row=3, start_column=1, end_row=5, end_column=1)

        # Sınıf ad
        self.ws.merge_cells(start_row=3, start_column=2, end_row=4, end_column=3)

        # Sınıf
        self.ws.merge_cells(start_row=5, start_column=2, end_row=5, end_column=3)

        # Kriter label
        self.ws.merge_cells(start_row=3, start_column=4, end_row=4, end_column=size + 3)

        # Kriter
        self.ws.merge_cells(start_row=6, start_column=1, end_row=14, end_column=1)
        for i in range(size):
            self.ws.merge_cells(
                start_row=5, start_column=4 + i, end_row=15, end_column=4 + i
            )
            self.ws.cell(5, 4 + i).alignment = Alignment(
                text_rotation=90, vertical="center", horizontal="center"
            )

        self.ws.merge_cells(
            start_row=3, start_column=size + 4, end_row=15, end_column=size + 4
        )

        self.ws.cell(3, size + 4).alignment = Alignment(
            text_rotation=90, vertical="center", horizontal="center"
        )

        self.ws["A3"] = "SINIF"
        self.ws["A6"] = "ÖLÇÜTLER"
        self.ws["B5"] = "SINIFI"
        self.ws["D3"] = "Öğrencide Gözlenecek kazanımlar"

        for i in range(5):
            self.ws["B" + str(i + 8)] = i + 1

        self.ws["C8"] = "ZAYIF"
        self.ws["C9"] = "KABUL EDİLEBİLİR"
        self.ws["C10"] = "ORTA"
        self.ws["C11"] = "İYİ"
        self.ws["C12"] = "ÇOK İYİ"

        self.ws["A15"] = "SIRA"
        self.ws["B15"] = "NO"
        self.ws["C15"] = "ADI SOYADI"

        self.ws["A1"].alignment = Alignment(horizontal="center")
        self.ws["A2"].alignment = Alignment(horizontal="center")

        self.ws["A3"].alignment = Alignment(
            text_rotation=90, vertical="center", horizontal="center"
        )
        self.ws["A6"].alignment = Alignment(
            text_rotation=90, vertical="center", horizontal="center"
        )

        self.ws["D3"].alignment = Alignment(horizontal="center")
        self.ws["D4"].alignment = Alignment(horizontal="center")

        self.ws["B4"].alignment = Alignment(horizontal="center")
        self.ws["B5"].alignment = Alignment(horizontal="center")

        self.ws["A1"] = metadata[5] + " EĞİTİM ÖĞRETİM YILI " + metadata[0]
        self.ws["A2"] = (
            metadata[4]
            + " DERSİ "
            + metadata[6]
            + " "
            + col.upper()
            + " NOTU DEĞERLENDİRME ÖLÇEĞİ"
        )
        self.ws["B3"] = metadata[3]

        self.ws.cell(3, size + 4).value = col.upper() + " PUANI"

    def add_dataframe(self, df):
        # TODO add rows from df
        pass

    def save(self, filename="taslak.xlsx"):
        self.wb.save(filename)
