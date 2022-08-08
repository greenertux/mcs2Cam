
import serial
import requests
import time
ser = serial.Serial('/dev/ttyS0', baudrate=115200, bytesize=8, parity="E")
ser.flushInput()
speakers = [] # keep list of active speakers here
companionIP = '127.0.0.1'
companionPort = '8888'
companionPath = '/press/bank/'
#pauseDuration = 0.7 # wait for specified time before sending command to cam

def readCommand(binary_data):
    if (binary_data == b'\x0b\x01\x00'):
        print ("speakerlist start")
        speakers = []
        return
    if (binary_data == b'\x0b\x01\x02'):
        print ("speakerlist end")
        return
    if (binary_data[0] == 11 and len(binary_data) > 3 and binary_data[3] != 0):
        print (str(binary_data[3]) + " is speaking")
        #speakers.append(binary_data[3])
        camToPosition(binary_data[3])
        #print (binary_data)
        #print ()
    print(binary_data)
    
def camToPosition(speaker):
        #chairmen
    if (speaker in range (1,8)):
        bank = speaker
        page = 13
        #delegate 1
    if (speaker in range (21,40)):
        bank = (speaker-20)
        page = 12
        #delegate 2
    if (speaker in range (41,60)):
        bank = (speaker-40)
        page = 11
        #guest
    if (speaker in range (71,80)):
        bank = (speaker-70) + 8
        page = 14
        
    sendCommand(page, bank)
    
def sendCommand(page, bank):
    requests.get('http://' + companionIP + ':' + companionPort + companionPath + str(page) + '/' + str(bank))

while True:
    try:
        #ser.read() # flush read buffer
        ser_bytes = ser.read(1)
        print (ser_bytes)
        bytes_to_read = int.from_bytes(ser_bytes, "little")
        print("Received " + str(bytes_to_read) + " bytes")
        data = ser.read(bytes_to_read)
        readCommand(data)
    except Exception as e: 
        print(e)
        #break
