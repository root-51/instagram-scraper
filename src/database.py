import sqlite3 as sql
import pandas as pd


def csvToDataframe(fileName):
    try:
        return pd.read_csv("resource/csv_input/" + fileName + ".csv")
    except Exception as e:
        print("cannot convert csv to dataframe:")
        print(e)
        return None
