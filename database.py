import sqlite3
import random

try:
    sqliteConnection = sqlite3.connect('Traccar_Client_Database.db')
    sqlite_create_table_query = '''CREATE TABLE Traccar_Client_Table (
                                RowNumber INTEGER PRIMARY KEY,
                                EventValue TEXT NOT NULL,
                                EventKey TEXT NOT NULL,
                                TimesExecuted INTEGER NOT NULL,
                                QValues REAL NOT NULL, 
                                Reward REAL
                                );'''

    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("sqlite connection is closed")




def insert_into(RowID, EventValue, EventKey, TimesExecutes, QValues, Reward):


    try:
            sqliteConnection = sqlite3.connect('Traccar_Client_Database.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sqlite_insert_with_param = """INSERT INTO Traccar_Client_Table
                              (RowNumber, EventValue, EventKey, TimesExecuted, QValues, Reward) 
                              VALUES (?, ?, ?, ?, ?, ?);"""

            data_tuple = (RowID, EventValue, EventKey, TimesExecutes, QValues, Reward)
            cursor.execute(sqlite_insert_with_param, data_tuple)
            sqliteConnection.commit()
            print("Python Variables inserted successfully into SqliteDb_developers table")

            cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

# def UpdateReward(SelectedEvent):
#     sqliteConnection = sqlite3.connect('Traccar_Client_Database.db')
#     cursor = sqliteConnection.cursor()
#     Reward = 1/
def getMaxValueEvent(stateId):
    stateId = str(stateId)
    try:
            sqliteConnection = sqlite3.connect('Traccar_Client_Database.db')
            cursor = sqliteConnection.cursor()

            cursor.execute("SELECT RowNumber FROM Traccar_Client_Table WHERE (QValues = (SELECT MAX(QValues) FROM Traccar_Client_Table))")
            numbers = cursor.fetchall()
            MyList = []


            for i in numbers:
                MyList.append(i[0])

            index = random.choice(MyList)
            cursor.close()

            return index

    except sqlite3.Error as error:
        print("Failed to access data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

