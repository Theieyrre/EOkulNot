import pandas as pd
from io import StringIO


class DataTable:
    def __init__(self):
        pass

    def insert_data(self, data):
        data_io = StringIO(data)
        print(data_io)
        df = pd.read_tsv(data_io)
        print(df.head(5))
