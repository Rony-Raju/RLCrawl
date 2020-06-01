# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from random import uniform
from abstraction import *
from constants import GUIActionType, SystemActionType, KeyCode, TargetType, TargetState, SelectorType
from ui_analysis import *


done = False
while not done:
    # Method that starts the application
    caps = {"platformName": "Android", "deviceName": "Android Emulator", "appPackage": "org.traccar.client",
            "appActivity": "org.traccar.client.Launcher", "platformVersion": "5.1.1", "noReset": True}

    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    #Getting the current state
    #print(get_current_state(driver))

    while True:
        #Generates the random integer that will be compared to the Home_Button_Probability
        Random = uniform(0.0, 1.0)

        #Home button probability
        Home_Button_Probability = .05
        if Random <= Home_Button_Probability:
          #At the specified state, generate the home event
          # " print(driver.query_app_state('org.traccar.client')) " gave us the value of 4 for the current state
          Selected_event = create_home_event('bb1e312877a55bb7ae166f4e0ba6d0bd84e360d6')
        else:
          Current_Events = get_available_events(driver)
          for events in Current_Events:







