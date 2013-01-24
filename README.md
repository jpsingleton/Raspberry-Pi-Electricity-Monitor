Raspberry-Pi-Electricity-Monitor
================================

Software for monitoring the electricity consumption of a home with a Raspberry Pi

James Singleton 2013 - http://unop.co.uk/dev/raspberry-pi-electricity-monitor

Copy the www folder to /var for httpd to host and the python file to anywhere.
Install http://pyserial.sourceforge.net/ with apt and plug in the receiver.

To run execute "sudo python raspberry-pi-electricity-monitor.py &" or add this to /etc/rc.local to run at boot.
Visit your pi in a browser to see the data.

Thanks to http://dygraphs.com/ for an awesome library and http://www.raspberrypi.org/ for the great hardware