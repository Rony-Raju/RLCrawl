# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from sqlalchemy import null

import database
from database import *
from appium import webdriver
from random import uniform
from abstraction import *
from constants import GUIActionType, SystemActionType, KeyCode, TargetType, TargetState, SelectorType
from ui_analysis import *
import sqlite3
from execution import *
from uuid import uuid4
import sqlite3
from QLearning_Functions import *

sqliteConnection = sqlite3.connect('Traccar_Client_Database.db')
cursor = sqliteConnection.cursor()
done = False
while not done:
    # Method that starts the application
    caps = {}
    caps["platformName"] = "Android"
    caps["deviceName"] = "Android Emulator"
    caps["appPackage"] = "org.traccar.client"
    caps["appActivity"] = "org.traccar.client.Launcher"
    caps["platformVersion"] = "5.1.1"
    caps["noReset"] = True

    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    count = 0
    sqliteConnection = sqlite3.connect('Traccar_Client_Database.db')
    cursor = sqliteConnection.cursor()
    # Getting the current state
    # print(get_current_state(driver))

    StateID = []
    while True:
        # Generates the random integer that will be compared to the Home_Button_Probability
        Random = uniform(0.0, 1.0)

        # Home button probability
        Home_Button_Probability = .05
        if Random <= Home_Button_Probability:
            # At the specified state, generate the home event
            # " print(driver.query_app_state('org.traccar.client')) " gave us the value of 4 for the current state
            Selected_event = create_home_event('bb1e312877a55bb7ae166f4e0ba6d0bd84e360d6')
        else:
            Current_State = get_current_state(driver)
            Current_Events = get_available_events(driver)
            Back_Event = create_back_event('bb1e312877a55bb7ae166f4e0ba6d0bd84e360d6')
            D = Executor(driver, 10, " ")
            print("Successfully retrieved the current events")
            for events in Current_Events:
                insert_into(count, str(events['actions']), str(events['precondition']['stateId']), 0, 500, 5)
                count += 1

        Current_Events = get_available_events(driver)
        Back_Event = create_back_event('bb1e312877a55bb7ae166f4e0ba6d0bd84e360d6')
        D = Executor(driver, 3, " ")

        #Retrieving the elements that have the max value from the table
        cursor.execute("SELECT RowNumber FROM Traccar_Client_Table WHERE (SELECT MAX(QValues) FROM Traccar_Client_Table)")
        tuple1 = cursor.fetchone()
        RowNum = tuple1[0]

        #Retrieving the index of the event for the RowNumber in the Database
        index = getMaxValueEvent(Current_State)
        print(index)

        Selected_event = Current_Events[index - 1]

        #executes the selected event
        D.execute(Selected_event)

        #Updating the number of times the event has been executed
        cursor.execute("UPDATE Traccar_Client_Table SET TimesExecuted = TimesExecuted + 1 WHERE (RowNumber= ?)", [index])
        sqliteConnection.commit()

        # # name = " '{'activityName': '.Launcher', 'stateId': 'crash'}' "
        # # SQL_Testing = " UPDATE Traccar_Client_Table SET EventKey = ? WHERE RowNumber = 0 "
        # # cursor.execute(SQL_Testing, [name])
        #

        #Getting the new state
        newState = get_current_state(driver)

        #Testing to see if it crashes
        if newState['stateId'] == 'crash':
            Selected_event['precondition']['stateId'] = 'crash'
            cursor.execute("UPDATE Traccar_Client_Table SET Reward = 0, QValues = 0 WHERE (RowNumber= ?)", [index])
            sqliteConnection.commit()

        #Getting the new available events
        New_Events = get_available_events(driver)

        #Getting the Discount Factor
        Gamma = calDiscountFactor(New_Events)

        #Inserting the new values into the table
        for n_events in New_Events:
            insert_into(count, str(n_events['actions']), str(n_events['precondition']['stateId']), 0, 500, 5)

        #Calculating the reward
        Reward = getReward(index)


        #Getting the Maximum Value from the New_Events
        MaxValue = getMaxValue(newState)

        #Getting the value from the Q_Value Function
        Q_Value = Reward + Gamma * MaxValue

        #Giving the new Q value to the event
        setQValue(Selected_event, Q_Value)



        break
    done = True
