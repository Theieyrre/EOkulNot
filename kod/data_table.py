import pandas as pd
from io import StringIO


class DataTable:
    def __init__(self, proje_columns_file, dersici_columns_file):
        self.proje_df = create_sub_df(proje_columns_file)
        self.dersici_df = create_sub_df(dersici_columns_file)

        self.columns = [
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

    def insert_data(self, data):
        data_io = StringIO(data)
        self.main_df = pd.read_csv(data_io, sep="\t", header=None)
        self.main_df.columns = self.columns
        print(self.main_df.head(5))


def create_sub_df(filename) -> pd.DataFrame:
    columns = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            columns.append(line.replace("\n", ""))
    return pd.DataFrame(columns=columns)
