# Software for monitoring the electricity consumption of a home with a Raspberry Pi
# James Singleton 2013 - 2024 - https://unop.uk - https://github.com/jpsingleton
# MIT licensed

import datetime
import struct
import time

# sudo apt-get install python3-serial
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
s2 = 'aa0200ad'
h2 = bytes.fromhex(s2)

fixedThreshold = 15
percentThreshold = 10

fRaw = open('/var/www/meterLogRaw.csv', 'a')
fFixed = open('/var/www/meterLogFixedThreshold.csv', 'a')
fPercent = open('/var/www/meterLogPercentageThreshold.csv', 'a')

lastValueF = 0
lastValueP = 0
maxValue = 25000
dateString = '%Y-%m-%d %H:%M:%S'

while True:
	try:
		ser.write(h2)
		data = ser.read(200)
		# Note, location in the data can vary by unit. Receivers can support multiple transmitters.
		# You may want to use the original values from the other files ([13:15]).
		watts = struct.unpack('<H', data[125:127])[0]
		if (watts > 0 and watts < maxValue):
			print(datetime.datetime.now().strftime(dateString), ',', watts, file=fRaw)
			fRaw.flush()
					
			deltaF = watts - lastValueF
			if (deltaF > fixedThreshold or deltaF < -fixedThreshold):
				print(datetime.datetime.now().strftime(dateString), ',', lastValueF, file=fFixed)
				time.sleep(1)
				print(datetime.datetime.now().strftime(dateString), ',', watts, file=fFixed)
				fFixed.flush()
				lastValueF = watts
			
			deltaP = watts - lastValueP
			threshold = lastValueP / percentThreshold
			if (deltaP > threshold or deltaP < -threshold):
				print(datetime.datetime.now().strftime(dateString), ',', lastValueP, file=fPercent)
				time.sleep(1)
				print(datetime.datetime.now().strftime(dateString), ',', watts, file=fPercent)
				fPercent.flush()
				lastValueP = watts
	except:
		pass
	time.sleep(7)
