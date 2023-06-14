import pandas as pd
from io import StringIO


class DataTable:
    def __init__(self, data):
        self.eokul_columns = [
            "Okul No",
            "Adı Soyadı",
            "1.Sınav",
            "2.Sınav",
            "1.Proje",
            "2.Proje",
            "1.Ders Et.Kat",
            "2.Ders Et.Kat",
            "3.Ders Et.Kat",
            "Proje-Ders Etk.Ort.",
            "Puanı",
            "Not Bilgisi Düğme",
        ]

        self.columns = ["Okul No", "Adı Soyadı"]

        data_io = StringIO(data)
        self.main_df = pd.read_csv(data_io, sep="\t", header=None)
        self.main_df.columns = self.eokul_columns

    def fill_sub_df(self, main_column, filename):
        # TODO spread remainder value to columns
        columns = self.columns.copy()
        columns.append(main_column)
        temp_df = self.main_df[columns]

        grade_columns = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                grade_columns.append(line.replace("\n", ""))

        temp_df = temp_df.reindex(columns=temp_df.columns.tolist() + grade_columns)

        for column in grade_columns:
            temp_df[column] = temp_df[main_column] // len(grade_columns)

        print(temp_df.head(5))
