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