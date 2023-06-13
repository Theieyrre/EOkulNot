import pandas as pd
from io import StringIO


class DataTable:
    def __init__(self):
        # TODO add column names
        pass

    def insert_header(self, data):
        pass

    def insert_data(self, data):
        data_io = StringIO(data)
        df = pd.read_csv(data_io, sep="\t", header=None)
        print(df.head(5))
