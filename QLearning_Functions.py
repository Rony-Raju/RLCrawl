import math
import sqlite3
import random

def calDiscountFactor(Available_Events):
    #Function for discount factor
    Discount_Factor = 0.9 * math.exp(-0.1 * (len(Available_Events) - 1))

    return Discount_Factor

def getReward(selectedEvent_index):

    sqliteConnection = sqlite3.connect('Traccar_Client_Database.db')
    cursor = sqliteConnection.cursor()


    x = cursor.execute("Select TimesExecuted FROM Traccer_Client_Table WHERE TimesExecuted = ?", [selectedEvent_index])

    #One divided by the total number of times the event has been executed
    reward = 1 / x

    return reward

def getMaxValue(stateId):
    stateId = str(stateId)

    sqliteConnection = sqlite3.connect('Traccar_Client_Database.db')
    cursor = sqliteConnection.cursor()

    cursor.execute("SELECT QValues FROM Traccar_Client_Table WHERE (QValues = (SELECT MAX(QValues) AND (EventKey = ?) FROM Traccar_Client_Table))", [stateId])

    #Using fetchone for now
    Values = cursor.fetchone()
    MyList = []
    for i in Values:
        MyList.append(i[0])

    Q_Value = random.choice(MyList)
    cursor.close()

    return Q_Value

def setQValue(Event, Q_Value):

    #Establishing the connection to the database
    sqliteConnection = sqlite3.connect('Traccar_Client_Database.db')
    cursor = sqliteConnection.cursor()

    


