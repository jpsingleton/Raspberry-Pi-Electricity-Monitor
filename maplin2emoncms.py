import serial
import struct
import datetime
import time
import urllib2

# Replace this with your emoncms Write API Key from the user account page
writeApiKey = 'WRITE API KEY GOES HERE'

# Change this if you use a different host or SSL (a must if not on a LAN)
baseAddress = 'http://localhost/emoncms'

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
s2 = 'aa0200ad'
h2 = s2.decode('hex')
maxValue = 25000

while True:
        try:
                ser.write(h2)
                data = ser.read(200)
                watts = struct.unpack('<H', data[13:15])[0]
                if (watts > 0 and watts < maxValue):
                        url = baseAddress + '/input/post.json?node=1&json={power:' + str(watts) + '}&apikey=' + writeApiKey
                        request = urllib2.Request(url)
                        response = urllib2.urlopen(request, timeout=6)
        except Exception:
                import traceback
                print traceback.format_exc()
                pass
        time.sleep(7)
