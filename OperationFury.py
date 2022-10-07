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
    weatherForecast = ["Rain","Snow","Sunny","Cloudy","Foggy","Storming","Icy"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition


weatherAlert = weather()
def vRS():
    if weatherAlert == "Icy":
        print("\n VRS has changed your alarm 30 minutes earlier based on the NWS forcast of" ,weatherAlert)



vRS()