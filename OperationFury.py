
#*****************************************************************************

#Import Libraries Here
from time import sleep #We imported the Sleep function from the Time Library
import random

#*****************************************************************************

#Welcome Screen
#Developer: Michael McCarthy
#Version: 1.0

"""
Our welcome Screen will start our program letting
drivers know that the InfoTechCenter OS is loading
"""

print("\n\nWelcome to Operation Fury InfoTech Center\n")
sleep(1.5)
print("\033[1;36m  \nOperation Fury's Operation System Booting Up")
for i in range(2):
    print("OS Booting up")
    sleep(.5)

#weather
#developer: Michael McCarthy
#Version 1.o

"""
Create a function for our weather using the
random.choice function to determine what the weather is
picking from a list - using if, elif, and else statements
to check the condition and print a specific print line
"""



#Weather condition list using the random.choice library
#to randomly chose a condition and storing it in its brain
def weather():
    weatherForecast = ["Rain","Snow","Sunny","Windy","Foggy","Storming","Icy"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition


weatherAlert = weather()
def vRS():
    if weatherAlert == "Icy":
        print("\n VRS has changed your alarm 30 minutes earlier based on the NWS forcast of" ,weatherAlert)
        print("VRS will only allow your car to go 30MPH")
    elif weatherAlert == "Snow":
        print("\n VRS has changed your alarm 15 minutes earlier based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 50MPH")
    elif weatherAlert == "Rain":
        print("\n VRS has changed your alarm 5 minutes earlier based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 60MPH")
    elif weatherAlert == "Windy":
        print("\n VRS has changed your alarm 5 minutes earlier based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 70MPH")
    elif weatherAlert == "Foggy":
        print("\n VRS has changed your alarm 5 minutes earlier based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 60MPH")
    elif weatherAlert == "Storming":
        print("\n VRS has changed your alarm 5 minutes earlier based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 60MPH")
    else:
        print("\n The weather today is", weatherAlert, ",let's Go!")
        print("VRS will only allow your car to go 90MPH")


vRS()


#Gasoline
#Programmer: Michael McCarthy
#Version 1.0

"""
Define a function to check our gas gauge and determine how far
we have until we need gasoline based on an if, elif, else
condition
"""




#Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#Variable calling the gasLevelGuage function to store value once
gasLevelIndicator = gasLevelGauge()

def listOfGasStations():
    gasStation = ["Shell", "Circle K", "Marathon", "Speedway", "Meijer"]
    GasStationNearby = random.choice(gasStation)
    return GasStationNearby
def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1, 25),1)
    milesToGasStationQuarter = round(random.uniform(26, 50),1)
    if gasLevelIndicator == "Empty":
        print("***WARNING YOU ARE ON EMPTY***")
        sleep(1)
        print("Calling Your Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("***WARNING***")
        sleep(1)
        print("You are running extremely low on gas")
        sleep(0.5)
        print("Checking google maps for nearest gas station")
        sleep(0.5)
        print("The nearest gas station is", listOfGasStations(), ".", listOfGasStations(), " is ", milesToGasStationLow, "miles away")
    elif gasLevelIndicator == "Quarter Tank":
        print("***WARNING***")
        sleep(1)
        print("You are running on a quarter tank of gas")
        sleep(0.5)
        print("Checking google maps for nearest gas station")
        sleep(0.5)
        print("The nearest gas station is", listOfGasStations(), ".", listOfGasStations(), " is ", milesToGasStationQuarter, "miles away")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is half full, you have plenty of gas to get where you want")
        print("The nearest gas station is", listOfGasStations(), ".", listOfGasStations(), " is ", milesToGasStationQuarter, "miles away")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is three quarter full, you have plenty of gas to get where you are going")
    else:
        print("Your gas tank is full, you have plenty of gas to get where you are going")


gasLevelAlert()