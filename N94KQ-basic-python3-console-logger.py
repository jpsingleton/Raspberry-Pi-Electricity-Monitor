import datetime
import struct
import time

# sudo apt-get install python3-serial
import serial

ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)

dateString = "%Y-%m-%d %H:%M:%S"

while True:
    try:
        ser.write(b"\xaa\x02\x00\xad")
        data = ser.read(200)
        watts = struct.unpack("<H", data[13:15])[0]

        # export PYTHONUNBUFFERED=true
        print(f"{datetime.datetime.now().strftime(dateString)},{watts}")
    except Exception:
        pass
    time.sleep(7)
