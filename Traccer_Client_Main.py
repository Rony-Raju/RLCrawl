# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from random import uniform
from constants import GUIActionType, SystemActionType, KeyCode, TargetType, TargetState, SelectorType


done = False
while not done:
    # Method that starts the application
    caps = {"platformName": "Android", "deviceName": "Android Emulator", "appPackage": "org.traccar.client",
            "appActivity": "org.traccar.client.Launcher", "platformVersion": "5.1.1", "noReset": True}

    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    while True:
        #Generates the random integer that will be compared to the Home_Button_Probability
        Random = uniform(0.1, 1.0)

        #Home button probability
        Home_Button_Probability = .05
        if Random <= Home_Button_Probability:
          Home_Button =



