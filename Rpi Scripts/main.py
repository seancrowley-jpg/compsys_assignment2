from sense_hat import SenseHat
import rainsensor
import blynklib
from time import sleep
BLYNK_AUTH = '6ZjvdpVlcMKx2Tq7XZoH-Jb1oCnwatbG'
sense = SenseHat()
sense.clear()
blynk = blynklib.Blynk(BLYNK_AUTH)
#Using The blynk App to control which script is run.

#First script sends Temp,pressure and humidity readings to thingspeak as well
#as the rain sensor reading connected to the RPi

#Sensehat LED matrix will turn blue for Rain notification method and green for the other
@blynk.handle_event('write V1')
def write_virtual_pin_handler(pin, value):
    if value[0]=="1":
        rainsensor.rain_notif()
    elif value[0]=="0":
        return

#The second script is the same as the first but with no rain sensor reading
@blynk.handle_event('write V2')
def write_virtual_pin_handler(pin, value):
    if value[0]=="1":
        rainsensor.sensor_read()

while True:
    blynk.run()