
import serial
import requests
import time
ser = serial.Serial('COM4', timeout=0.5)
ser.flushInput()
speakers = [] # keep list of active speakers here
companionIP = '127.0.0.1'
companionPort = '8888'
companionPath = '/press/bank/'
pauseDuration = 0 # wait for specified time before sending command to cam

def readCommand(ascii_data):
    if (ascii_data.startswith("clear")):
        print("Clear command")
    elif (ascii_data.startswith("P") and ascii_data.endswith("M")):
        speaker = ascii_data[1:4]
        print("Speaker " + speaker + " started speaking")
        speakers.append(speaker)
        printSpeakers()
        evaluateSpeakers()
    elif (ascii_data.startswith("P") and ascii_data.endswith("P")):
        speaker = ascii_data[1:4]
        print("Speaker " + speaker + " started speaking")
        speakers.append(speaker)
        printSpeakers()
        evaluateSpeakers()
    elif (ascii_data.startswith("R")):
        speaker = ascii_data[1:4]
        print("Speaker " + speaker + " stopped speaking")
        speakers.remove(speaker)
        printSpeakers()
        evaluateSpeakers()

def printSpeakers():
    print("Active speakers: " + str(speakers))

def evaluateSpeakers(): # set camera based on current situation
    if (len(speakers) > 0):
        if (speakers[-1] == '017'): return
        print("Setting speaker view")
        sendCommand(1,3)
    
    if (len(speakers) == 0):
        print("Setting totale view")
        sendCommand(1,2)
        
#seat 01 - ID49
    elif (speakers[-1] == '049'):
        print("Setting speaker 049 view")
        sendCommand(2,2)
#seat 02 - ID48
    elif (speakers[-1] == '048'):
        print("Setting speaker 048 view")
        sendCommand(2,3)
#seat 03 - ID47
    elif (speakers[-1] == '047'):
        print("Setting speaker 047 view")
        sendCommand(2,4)
#seat 04 - ID46
    elif (speakers[-1] == '046'):
        print("Setting speaker 046 view")
        sendCommand(2,5)
#seat 05 - ID45
    elif (speakers[-1] == '045'):
        print("Setting speaker 045 view")
        sendCommand(2,6)
#seat 06 - ID44
    elif (speakers[-1] == '044'):
        print("Setting speaker 044 view")
        sendCommand(2,7)
#seat 07 - ID43
    elif (speakers[-1] == '043'):
        print("Setting speaker 043 view")
        sendCommand(2,8)
#seat 08 - ID42
    elif (speakers[-1] == '042'):
        print("Setting speaker 042 view")
        sendCommand(2,10)
#seat 09 - ID41
    elif (speakers[-1] == '041'):
        print("Setting speaker 041 view")
        sendCommand(2,11)
#seat 10 - ID40
    elif (speakers[-1] == '040'):
        print("Setting speaker 040 view")
        sendCommand(2,12)
#seat 11 - ID39
    elif (speakers[-1] == '039'):
        print("Setting speaker 039 view")
        sendCommand(2,13)
#seat 12 - ID38
    elif (speakers[-1] == '038'):
        print("Setting speaker 038 view")
        sendCommand(2,14)
#seat 13 - ID37
    elif (speakers[-1] == '037'):
        print("Setting speaker 037 view")
        sendCommand(2,15)
#seat 14 - ID36
    elif (speakers[-1] == '036'):
        print("Setting speaker 036 view")
        sendCommand(2,16)
#seat 15 - ID35
    elif (speakers[-1] == '035'):
        print("Setting speaker 035 view")
        sendCommand(2,18)
#seat 16 - no unit
        
#seat 17 - ID34
    elif (speakers[-1] == '034'):
        print("Setting speaker 034 view")
        sendCommand(2,20)
#seat 18 - no unit
        
#seat 19 - ID33
    elif (speakers[-1] == '033'):
        print("Setting speaker 033 view")
        sendCommand(3,2)
#seat 20 -  no unit
        
#seat 21 - ID01
    elif (speakers[-1] == '001'):
        print("Setting speaker 001 view")
        sendCommand(3,3)      
#seat 22 - no unit
        
#seat 23 - no unit
        
#seat 24 - ID02
    elif (speakers[-1] == '002'):
        print("Setting speaker 002 view")
        sendCommand(3,6)
#seat 25 - ID03
    elif (speakers[-1] == '003'):
        print("Setting speaker 003 view")
        sendCommand(3,7)
#seat 26 - ID04
    elif (speakers[-1] == '004'):
        print("Setting speaker 004 view")
        sendCommand(3,8)
#seat 27 - ID05
    elif (speakers[-1] == '005'):
        print("Setting speaker 005 view")
        sendCommand(3,10)
#seat 28 - ID06
    elif (speakers[-1] == '006'):
        print("Setting speaker 006 view")
        sendCommand(3,11)
#seat 29 - ID07
    elif (speakers[-1] == '007'):
        print("Setting speaker 007 view")
        sendCommand(3,12)
#seat 30 - ID08
    elif (speakers[-1] == '008'):
        print("Setting speaker 008 view")
        sendCommand(3,13)
#seat 31 - ID09
    elif (speakers[-1] == '009'):
        print("Setting speaker 009 view")
        sendCommand(3,14)
#seat 32 - ID10
    elif (speakers[-1] == '010'):
        print("Setting speaker 010 view")
        sendCommand(3,15)
#seat 33 - ID11
    elif (speakers[-1] == '011'):
        print("Setting speaker 011 view")
        sendCommand(3,16)
#seat 34 - ID12
    elif (speakers[-1] == '012'):
        print("Setting speaker 012 view")
        sendCommand(3,18)
#seat 35 - ID13
    elif (speakers[-1] == '013'):
        print("Setting speaker 013 view")
        sendCommand(3,19)
#seat 36 - ID14
    elif (speakers[-1] == '014'):
        print("Setting speaker 014 view")
        sendCommand(3,20)
#seat 37 - ID15
    elif (speakers[-1] == '015'):
        print("Setting speaker 015 view")
        sendCommand(3,21)
#seat 38 - ID16
    elif (speakers[-1] == '016'):
        print("Setting speaker 016 view")
        sendCommand(3,22)
#seat 39 - ID17 (PPT PC)
    elif (speakers[-1] == '017'):
        print("Speaker 017 is not allowed to show, setting totale view")
        sendCommand(1,2)        ###Set to 'totale view', did not agree to show closeup###
    
def sendCommand(page, bank):
    time.sleep(pauseDuration)
    requests.get('http://' + companionIP + ':' + companionPort + companionPath + str(page) + '/' + str(bank))

while True:
    try:
        ser_bytes = ser.read(10000)
        splitted_bytes = ser_bytes.split(b'\r')
        for i in splitted_bytes:
            decoded_bytes = i.decode("ascii", errors='ignore')
            readCommand(decoded_bytes)
    except Exception as e: 
        print(e)
        #break
