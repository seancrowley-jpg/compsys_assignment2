from gpiozero import InputDevice, CPUTemperature
from sense_hat import SenseHat
from time import sleep
from urllib.request import urlopen
import json

sense = SenseHat()
rain_sense = InputDevice(18)
sense.clear(0,255,0)
humid = round(sense.get_humidity(),2)
cpu = CPUTemperature()
#Taking 10 fromt the temp value to compensate for cpu heat
temp = sense.get_temperature() - 10
#formula for calculating a more accruate temp
temp_calculated = round(temp - ((cpu.temperature - temp)/5.466),2)
press = round(sense.get_pressure(),2)

WRITE_API_KEY='HOZ64RVZSJ7EY433'

baseURL='https://api.thingspeak.com/update?api_key=%s' % WRITE_API_KEY

def writeData(temp_calculated,humid,press):
    # Sending the data to thingspeak in the query string
    conn = urlopen(baseURL + '&field1=%s&field2=%s&field3=%s' % (temp_calculated,humid,press))
    print(conn.read())
    # Closing the connection
    conn.close()

def writeData_rain_sense(temp_calculated,humid,press,rain):
    # Sending the data to thingspeak in the query string
    conn = urlopen(baseURL + '&field1=%s&field2=%s&field3=%s&field4=%s' % (temp_calculated,humid,press,ra$
    print(conn.read())
    # Closing the connection
    conn.close()

#functions Run on the main file. Sends the sensor data to ThingSpeak
#Pressure data can sometimes appear as zero when first starting the function
#restarting seems to fix it
def sensor_read():
    while True: 
        sense.clear(0,255,0)
        print("Temperature: " + str(round(temp_calculated,2)))
        print("Humidity: " + str(round(humid,2)))
        print("Pressure: " + str(round(press,2)))
        writeData(temp_calculated,humid,press)
        #Terminates the function and returns to the main script 
        #if the button on the SenseHat is moved/pressed
        for event in sense.stick.get_events():
            sense.clear()
            return
        sleep(5)

def rain_notif():
    while True:
    sense.clear(0,0,255)
        rain = 0
        print("Temperature: " + str(round(temp_calculated,2)))
        print("Humidity: " + str(round(humid,2)))
        print("Pressure: " + str(round(press,2)))
        #If enough Water is detected on the surface of the rain sensor 
        #attached to the RPi the rain Variable will be set to 1 and then 
        #the write data function is called with the rain vaibale included
        if not rain_sense.is_active:
            print("Rain")
            rain = 1
            writeData_rain_sense(temp_calculated,humid,press,rain)
            sense.show_message("RAIN!!", text_colour=[255,0,0])
            continue
        writeData_rain_sense(temp_calculated,humid,press,rain)
        #Terminates the function and returns to the main script 
        #if the button on the SenseHat is moved/pressed
        for event in sense.stick.get_events():
            sense.clear()
            return
        sleep(5)
