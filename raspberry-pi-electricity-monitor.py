# Software for monitoring the electricity consumption of a home with a Raspberry Pi
# James Singleton 2013 - 2015 - https://unop.uk - https://github.com/jpsingleton
# MIT licensed

import serial
import struct
import datetime
import time

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
s2 = 'aa0200ad'
h2 = s2.decode('hex')

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
		watts = struct.unpack('<H', data[13:15])[0]
		if (watts > 0 and watts < maxValue):
			print >> fRaw, datetime.datetime.now().strftime(dateString), ',', watts
			fRaw.flush()
					
			deltaF = watts - lastValueF
			if (deltaF > fixedThreshold or deltaF < -fixedThreshold):
				print >> fFixed, datetime.datetime.now().strftime(dateString), ',', lastValueF
				time.sleep(1)
				print >> fFixed, datetime.datetime.now().strftime(dateString), ',', watts
				fFixed.flush()
				lastValueF = watts
			
			deltaP = watts - lastValueP
			threshold = lastValueP / percentThreshold
			if (deltaP > threshold or deltaP < -threshold):
				print >> fPercent, datetime.datetime.now().strftime(dateString), ',', lastValueP
				time.sleep(1)
				print >> fPercent, datetime.datetime.now().strftime(dateString), ',', watts
				fPercent.flush()
				lastValueP = watts
	except:
		pass
	time.sleep(7)

