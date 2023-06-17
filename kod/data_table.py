import pandas as pd
from io import StringIO
import random


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

    def fill_sub_df(self, main_column, grade_columns) -> pd.DataFrame:
        columns = self.columns.copy()
        columns.append(main_column)
        temp_df = self.main_df[columns]

        temp_df = temp_df.reindex(
            columns=["Sıra"] + temp_df.columns.tolist() + grade_columns
        )

        for column in grade_columns:
            temp_df[column] = temp_df[main_column] // len(grade_columns)

        temp_df["Kalan Not"] = temp_df[main_column] % len(grade_columns)

        for index, row in temp_df[temp_df[main_column] > 0].iterrows():
            g_columns = grade_columns.copy()
            for i in range(int(row["Kalan Not"])):
                idx = random.randint(0, len(g_columns) - 1)
                update_column = g_columns[idx]
                temp_df.loc[index, update_column] = (
                    int(temp_df.loc[index, update_column]) + 1
                )
                g_columns.remove(g_columns[idx])

        temp_df = temp_df.drop(columns=["Kalan Not"])

        col_list = list(temp_df.columns)
        x, y = col_list.index(main_column), col_list.index(grade_columns[-1])
        col_list[y], col_list[x] = col_list[x], col_list[y]
        temp_df = temp_df[col_list]

        temp_df["Sıra"] = range(1, len(temp_df["Okul No"]) + 1)
        return temp_df

    def write_excel(self, df, filename):
        df.to_excel(filename)
