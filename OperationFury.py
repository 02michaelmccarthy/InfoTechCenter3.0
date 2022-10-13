#Gasoline
#Programmer: Michael McCarthy
#Version 1.0

"""
Define a function to check our gas gauge and determine how far
we have until we need gasoline based on an if, elif, else
condition
"""

#import library here
import random
from time import sleep


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