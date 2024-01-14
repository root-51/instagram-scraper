import sqlite3 as sql
import pandas as pd


def csvToDataframe(fileName):
    try:
        return pd.read_csv("resource/csv_input/" + fileName + ".csv")
    except Exception as e:
        print("cannot convert csv to dataframe:")
        print(e)
        return None


def createDatebase(databaseName):
    return sql.connect("databases/" + databaseName + ".db")


def dataframeToDatabase(dataframe, db_name, table_name):
    conn = sql.connect("databases/" + db_name + ".db")
    dataframe.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.commit()
    conn.close()

def updateNumOfPosts(enterprise_name, value):
    conn = sql.connect("databases/test01.db")
    cursor = conn.cursor()
    query = f"UPDATE Enterprise SET num_of_posts = {value} WHERE enterprise_name = '{enterprise_name}'; "
    cursor.execute(query)
    conn.commit()
    conn.close()