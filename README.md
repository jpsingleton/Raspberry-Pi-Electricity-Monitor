Raspberry Pi Electricity Monitor
================================

*Update:* Maplin have discontinued the electricity monitor used here (N94KQ) and Maplin don't even exist now.

I've added a basic Python 3 version (`N94KQ-basic-python3-console-logger.py`) that outputs to the console (if you set `PYTHONUNBUFFERED=true`).

There is also a Python 3 port of the original version (thanks to Dave Cutliffe).

---

Software for monitoring the electricity consumption of a home with a Raspberry Pi (or other Linux machine) and a Maplin electricity monitor (N94KQ).

Full write up: [unop.uk/dev/raspberry-pi-electricity-monitor](https://unop.uk/dev/raspberry-pi-electricity-monitor/)

Copy the `www` folder to `/var` for httpd to host and the python file to anywhere.
Install `pyserial` with `apt` and plug in the receiver.

To run execute `sudo python raspberry-pi-electricity-monitor.py &` or add this to `/etc/rc.local` to run at boot.
Visit your pi in a browser to see the data.

---

I've added a new script (`maplin2emoncms.py`) which you can use to push the data to [OpenEnergyMonitor](http://openenergymonitor.org) [emoncms](https://github.com/emoncms/emoncms) running on the Pi.

---

Thanks to [dygraphs](http://dygraphs.com) for an awesome library and [Raspberry Pi](https://www.raspberrypi.org) for the great hardware.

MIT licensed

See also [this alternative](http://electroncastle.com/wp/?p=1808).
