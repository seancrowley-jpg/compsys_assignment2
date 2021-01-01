# compsys_assignment2

Repository for Rain Detection / Weather Sensor IoT Device.

Here you can find the code / resources I used to set up a Home weather monitoring/ rain notifier IoT device.

BLE Scanner Setup:
Firstly, the BLE Scanner folder contains the Shell scripts to turn on and run the Raspberry Pi’s Bluetooth sensor. The Scripts configure the Sensor to run as an Eddystone beacon.
Running the eddy_start script will advertise the website used in the project. Using a Beacon Scanner on your smart phone (I used this one on the Google Play Store 
https://play.google.com/store/apps/details?id=com.bridou_n.beaconscanner&hl=en_IE&gl=US) you should be able to get a link directly to the website.

MATLAB Analysis Code:
The next folder is the MATLAB Analysis Code I used on the ThingSpeak IoT platform to run a series of API calls to OpenWeaterMap (https://openweathermap.org).
Each file scrapes a different piece of weather data from the OpenWeatherMap API.
The different files are used in separate MATLAB apps on the site as combining them into the one app on the ThingSpeak site causes a URL request error. 
This Code is run every 10 minutes using ThingSpeak’s TimeControl feature.

Rpi Scripts:
This Folder contains the two scripts that are used to retrieve the sensor data and send it to ThingSpeak. The file called “main.py” is the file that should be run on the Raspberry Pi.
This file uses the Blynk IoT platform to wireless control the app. It is used to pick which method to use, one that only reads and sends temp, humidity and pressure data to
ThingSpeak or another that sends the same data but also detects whether is water on the rain sensor pad. The React tool on ThingSpeak then sends a ThingHTTP to a webhook on 
IFTTT when rain is detected to alert you when it is raining. The second file “rainsensor.py” holds methods/functions that are imported into the main file. In the “rainsensor.py”
file I used a formula to get a better reading from the SenseHat temperature sensor that I found at the following link:
( https://github.com/initialstate/wunderground-sensehat/wiki/Part-3.-Sense-HAT-Temperature-Correction ).
This is because the heat from the CPU of the Raspberry Pi disrupts the reading from temperature sensor.

WebSite files:
This folder contains the files for the node.js web app used to display the data for the Raspberry Pi scripts as well as the scripts for the MATLAB analysis code apps.
The site was created on the Glitch platform using Handlebars and Semantic UI for the CSS. The site has two web pages the dashboard displays embedded charts from ThingSpeak.
The forecast page displays widgets from ThingSpeak that show current weather data. It also shows tomorrows weather data using a fetch request to
the OpenWeatherMap API ( https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch ). The method is written between a script tag in HTML of the forecast page.
This is used to display tomorrows weather data.

PDF:
The Pdf file shows a block level representation of the project. Every device, piece of software and how they relate to each other is show in the diagram.

Known Bugs: 
Sometimes the pressure reading from the SenseHat will read as zero. Restarting the script usually fixes this.

Hardware/Software Used:
            Raspberry Pi 3 B+
            SenseHat
            LM393 Rain Drops Sensor Weather Moisture Monitor Sensor Humidity Sensitivity Module Nickeled Plate 3.3-5V for Arduino
            Blynk Iot platform
            ThingSpeak Iot platform
            Glitch

Other resources Used:
SenseHat GPIO Pins: https://pinout.xyz/pinout/sense_hat#
Rain Sensor Setup: https://www.terraelectronica.ru/pdf/show?pdf_file=%252Fz%252FDatasheet%252FS%252FSnow%2B%2526%2BRaindrops%2BDetection.pdf 
