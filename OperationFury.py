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

number = random.randint(1,20)

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
        print("The nearest gas station is", listOfGasStations(), ". ", listOfGasStations(), " is ", number, " miles away")

gasLevelAlert()