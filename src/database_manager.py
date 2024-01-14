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
    conn = connectDatabase(db_name)
    dataframe.to_sql(table_name, conn, if_exists="replace", index=False)
    finishQuery(conn)


def updateNumOfPosts(enterprise_name, value):
    conn = connectDatabase("test01")
    cursor = createCursor(conn)
    query = f"UPDATE Enterprise SET num_of_posts = {value} WHERE enterprise_name = '{enterprise_name}'; "
    cursor.execute(query)
    finishQuery(conn)


def connectDatabase(database_name: str) -> sql.Connection:
    return sql.connect(f"databases/{database_name}.db")


def createCursor(conn: sql.Connection) -> sql.Cursor:
    return conn.cursor()


def finishQuery(conn: sql.Connection) -> None:
    conn.commit()
    conn.close()


def getTable(db_name: str, table_name: str) -> list:
    conn = connectDatabase(db_name)
    cursor = createCursor(conn)
    cursor.execute(f"SELECT * FROM {table_name}")
    data = cursor.fetchall()
    finishQuery(conn)
    return data
