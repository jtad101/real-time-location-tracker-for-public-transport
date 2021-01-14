from __future__ import print_function
import serial
import pynmea2
import paho.mqtt.publish as publish
import string
import time

# Assigns the serial port ttyACM0 with baud rate 9600 and time out of 0.5 seconds.
serialStream = serial.Serial("/dev/ttyACM0", 9600, timeout=0.5)
while(1):

#Thingspeak channel ID, write API key,MQTT API key. 
    channelID = "896656"
    writeAPIKey = "HOC815LAIRP0DA2H"
    mqttHost = "mqtt.thingspeak.com"
    mqttUsername = "Bus tracking data"
    mqttAPIKey = "CCBI1R47UJINGC0O"
    tTransport = "websockets"
    tPort = 80
    topic = "channels/" + channelID  + "/publish/" + writeAPIKey
#Reads the data and decodes them to original string
    sentence = serialStream.readline().decode()
    if sentence.find('GGA') > 0:
# Converts the data to NMEA standards to be read by Thingspeak cloud server
        data = pynmea2.parse(sentence)
        payload = "field1=" + str(data.latitude) + "&field2=" + str(data.longitude\
)
#Publish/write the data to Thingspeak cloud server.
        publish.single(topic, payload, hostname=mqttHost, transport=tTransport, po\
rt=tPort,auth={'username':mqttUsername,'password':mqttAPIKey})
        print ("Latitude = ", data.latitude,"Longitude = ", data.longitude)
#sleeps for 15 seconds as Thingspeak free lisence only allows updating the data every 15 seconds.        
	time.sleep(15)