Raspberry-Pi-Electricity-Monitor
================================

Software for monitoring the electricity consumption of a home with a Raspberry Pi

Full write up: [unop.uk/dev/raspberry-pi-electricity-monitor](https://unop.uk/dev/raspberry-pi-electricity-monitor/)

Copy the `www` folder to `/var` for httpd to host and the python file to anywhere.
Install `pyserial` with `apt` and plug in the receiver.

To run execute `sudo python raspberry-pi-electricity-monitor.py &` or add this to `/etc/rc.local` to run at boot.
Visit your pi in a browser to see the data.

You can also use `maplin2emoncms.py` to push the data to [emoncms](https://github.com/emoncms/emoncms).

---

Thanks to [dygraphs](http://dygraphs.com) for an awesome library and [Raspberry Pi](https://www.raspberrypi.org) for the great hardware.

MIT licensed

See also [this alternative](http://electroncastle.com/wp/?p=1808).
