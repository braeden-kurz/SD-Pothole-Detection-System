import serial
import time
import string
import pynmea2
import os.path

# Set port to /dev/ttyAMA0
port="/dev/ttyAMA0"
# Open serial port
ser=serial.Serial(port,baudrate=9600,timeout=5.0)

while True:
    # Decode incoming data from byte to string datatype
    try:
        newdata=ser.readline().decode().strip()
    except Exception as e:
        print(e)
    
    # If this label is detected parse the data and display the lat and
    # lon data
    if newdata[0:6]=='$GPRMC':
        try:
            # Parse the longitude & latitude data from the GPRMC label
            newmsg=pynmea2.parse(newdata)
            lat=round(newmsg.latitude,6)
            lng=round(newmsg.longitude,6)
            # Compile message, print it, and write it to our log file
            gps="Latitude="+str(lat)+" and Longitude="+str(lng)
            with open('pothole-log.txt','a') as log:
                log.write(gps)
            print(gps)
        except Exception as e:
            print(e)
    time.sleep(0.1)
