#import required functions.
import os, socket, sys, argparse, time
from threading import Thread

Logging_Enabled = bool
Logging_Enabled = True

#ask user for targetbto scan.
__Target = raw_input('[-] Enter target IP/web address: ')
__Target_Resolve = socket.gethostbyname(__Target)

#deafult ports to check
__Default_Ports = [13,15,21,22,25,53,80,123,125,110,135,137,139,443,1433,1434,8080]

#set timeout for each connection
__SetTimeOut = input('[-] Enter timeout in sec: ')

#print initial data
print("\n[-] Resolved " + str(__Target) + " to IP address: " + str(__Target_Resolve)) 

#Connection Function
def __Connect(__Target, __Target_Port, __SetTimeOut):
	Logging_Enabled = bool
	Logging_Enabled = True
	try:
		socket.setdefaulttimeout(__SetTimeOut)
		__Soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		__Soc.connect((__Target_Resolve, __Target_Port))
		__Soc.send('GET /index.html')
		__Reply = __Soc.recv(1024)
		__Soc.close()
		print("[-] Recieved " + str(__Reply) + " from " + str(__Target_Resolve) + " / " + str(__Target) + " on port " + str(__Target_Port))
		if(str(args.Logging_Enabled) == 'False'):
			__WriteLog("[-] Recieved " + str(__Reply) + " \n\tfrom " + str(__Target_Resolve) + " / " + str(__Target) + " on port " + str(__Target_Port))
	except (Exception) as e:
		print("[-] Error: " + __Target + " on port " + str(__Default_Ports[i]) + " : " + str(e))
		if(str(args.Logging_Enabled) == 'False'):
			__WriteLog("[-] Error: " + __Target + " on port " + str(__Default_Ports[i]) + " : " + str(e))

def __WriteLog(__Data):
	LogOpen = open("log.txt", "a")
	LogOpen.write(str(__Data) + "\n")
	LogOpen.close()


Logging_Enabled = bool
Logging_Enabled = True
Port_Specific = 0

__Parser = argparse.ArgumentParser()
__Parser.add_argument('-l', action='store_false', dest='Logging_Enabled')
__Parser.add_argument('-p', action='store', dest='Port_Specific', type=int)
args = __Parser.parse_args()

if(str(args.Logging_Enabled) == 'False'):
	__WriteLog("PScan.py initiated at " + time.asctime())

i = 1
while (i < len(__Default_Ports)):
	T = Thread(__Connect(__Target, __Default_Ports[i], __SetTimeOut))
	T.start()
	i = i + 1