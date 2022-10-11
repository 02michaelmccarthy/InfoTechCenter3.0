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

#Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#Variable calling the gasLevelGuage function to store value once
gasLevelIndicator = gasLevelGauge()

def gasLevelAlert():
    if gasLevelIndicator == "Empty":
        print("***WARNING YOU ARE ON EMPTY***\n Calling Emergency Contact")

gasLevelAlert()