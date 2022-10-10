
#Welcome Screen
#Developer: Michael McCarthy
#Version: 1.0

"""
Our welcome Screen will start our program letting
drivers know that the InfoTechCenter OS is loading
"""

#Import Libraries Here
from time import sleep #We imported the Sleep function from the Time Library

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

#Import Libraries here
import random
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

