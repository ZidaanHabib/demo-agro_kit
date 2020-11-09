
from time import sleep
import agro_kit as ag
import os


def setup():
    """ Method to be used to intialise variables before main() """
    global exit     #define exit flag to termiante program
    exit = False
    print("Welcome to the Demo. This a basic overview of some of the functionality in our API.\n" )     # Welcome message
    global myAG     # this object will be used in the main method
    myAG = ag.AgroKit()


def main():
    """ Main method that prompts user for input and does what they want """
    global exit           # use global exit var
    global myAG           #use global AgroKit object isntantiated in setup()
    options = '''1) Read Moisture\n2) Read Lux\n3) Read GPS RMC Message\
    \n4) Full Read \n5) View profiles file\n6) Create profile\n7) Load profile\n\
    8) Full Read and check within range \n9) Read and log data\n\
    10) View readings logged in last 24hrs\nq) exit'''     #these are the user commands
    print(options)
    cmd = input("\nEnter a command:\n")      #prompt use to enter number of command they want to use
    print("\n")
    if cmd == '1':              
        print("Moisture: "+  str(myAG.MS.singleRead()))
    elif cmd == '2':
        light = myAG.LS.singleReadLux()
        print("Lux: " + str(light))
    elif cmd == '3':
        print(myAG.GPS.getRMC())
    elif cmd == '4':
        myAG.read()
    elif cmd == '5':
        os.system("more profiles.json")
    elif cmd == '6':
        name = input("Enter a profile name:\n")
        minMoist = eval(input("Enter min moisture:\n"))
        maxMoist = eval(input("Enter max moisture:\n"))
        minLux = eval(input("Enter min lux:\n"))
        maxLux = eval(input("Enter max lux:\n"))
        ag.createProfile(name, minMoist, maxMoist, minLux, maxLux)
    elif cmd == '7':
        name = input("Enter profile name to load:\n")
        myAG.loadProfile(name)
        print('Min Moisture: ' + str(myAG.MIN_MOISTURE) + "\tMax Moisture: " + str(myAG.MAX_MOISTURE)\
        + "\tMin Lux: " + str(myAG.MIN_LUX) + "\tMax Lux: " + str(myAG.MAX_LUX))

    elif cmd == '8':
        reading = myAG.read()
        msg = ['']
        ok = myAG.readingOK(reading, msg)
        print(msg[0])
    elif cmd == '9':
        gll = myAG.GPS.getGLL()
        rmc = myAG.GPS.getRMC()
        gga = myAG.GPS.getGGA()
        moist = myAG.MS.singleRead()
        lux = myAG.LS.singleReadLux()
        myAG.logData(rmc, gga, gll, moist, lux)
    elif cmd == '10':
        myAG.last24Hrs('log.txt')
    else:
        exit = True

if __name__ == "__main__":
    setup()    #call set up method to intialise exit flag and myAG
    while not exit:     #loop until exit flag true
        main()
        sleep(0.2)
        print("\n")
