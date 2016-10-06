Timeline
--------
![alt tag](master-thesis-timeline.png)

LogBook
-------
- [August](https://github.com/gtrdp/masters-thesis-guntur/blob/master/LogBook/00-august.md)
- [September](https://github.com/gtrdp/masters-thesis-guntur/blob/master/LogBook/01-september.md)
- [October](https://github.com/gtrdp/masters-thesis-guntur/blob/master/LogBook/02-october.md)
- [November](https://github.com/gtrdp/masters-thesis-guntur/blob/master/LogBook/03-november.md)
- [December](https://github.com/gtrdp/masters-thesis-guntur/blob/master/LogBook/04-december.md)
- [January](https://github.com/gtrdp/masters-thesis-guntur/blob/master/LogBook/05-january.md)
- [February](https://github.com/gtrdp/masters-thesis-guntur/blob/master/LogBook/06-february.md)

October #1
----------
- **Mon Oct  3 11:00:43 CEST 2016**
	- Try to analyze the data: doing preprocessing.
		- Installing `SciPy`: http://www.lowindata.com/2013/installing-scientific-python-on-mac-os-x/
		- use `pip install --user` to install the packages as current user.
		- Good site to test regex: https://regex101.com/
	- Tried to run the VAD on matlab, but got a problem on `sp2max` as it must be compiled from `c` source code.

- **Tue Oct  4 10:28:45 CEST 2016**
	- Fix the experimental setup according to doable scenario.
	- **Possible research** Probably change the scanning period to 5 minutes.
	- Continue working on data processing.
		- Finally got the working code.

- **Wed Oct  5 10:00:37 CEST 2016**
	- Call Niels:
		- Turns out that multiple APs are using the same `eduroam` as their SSID, however, they have different MAC addresses.
		- Is it possible for android to distinguish between APs with same SSID?
			- Possible, using `getBSSID()` method: https://developer.android.com/reference/android/net/wifi/WifiInfo.html#getBSSID%28%29
		- **Possible discussion** does weather affect wifi connection?
		- experiment with randomization period, as mentioned in the paper. This is important to get the optimal scanning period of WiFi.
		- Define the appropriate scanning time and place.
	- Look for a WiFi dongle that support monitor mode.
		- Built in RasPi 3 WiFi does not support monitor mode: https://www.reddit.com/r/raspberry_pi/comments/4ah4oi/psa_the_raspberry_pi_3s_embedded_wifi_card_does/
		- `RTL8188EU` does not work on monitoring mode: http://raspberrypi.stackexchange.com/questions/8578/enable-monitor-mode-in-rtl8188cus-realtek-wifi-usb-dongle
		- **ordered** This might be an option, although it has the same chipset with tenda micro: http://www.ebay.com/itm/150M-USB-WiFi-Wireless-Adapter-LAN-w-Antenna-Raspberry-Pi-2-B-ralink-rt5370Chip-/261561868698?hash=item3ce64d619a:g:hTMAAOxyP4dTdiDR
	- **Learn** how to get the data from the VAD. As it draws an image, it should give a clear data.
	- Learning and Getting the `crowdpp` code to work.
		- Highlight: line `391` the `AsyncTask` for crowd counting.
		- Highlight: line `252` when the event of recording start.
		- What to get: feature extraction using MFCC and YIN; counting people using the unsupervised algorithm.
	- **Important** IEEE public list of OUI: https://regauth.standards.ieee.org/standards-ra-web/pub/view.html#registries
	- **Important** It is not possible to infer the device type from mac address, but only the manufacturer:
		- https://www.experts-exchange.com/questions/23644286/How-to-determine-if-possible-the-device-type-by-MAC-address.html#answer22221053

- **Thu Oct  6 11:03:23 CEST 2016**
	- Working on Crowd++.
		- Using the code from the original version.

- **Fri**
	- Revising thesis

- **Sat**
	- Experiment for both social density and mac address randomization.

- **Sun**
	- Deadline Chapter 2.

October #2
----------
- **Fri**
	- Meeting with Prof Aiello and Prof Kas.
		- Prepare the schedule for the next meeting.
		- Possible ground truth is official document from stakeholders.
	- Listing the lecturers for email.


October #3
----------

October #4
----------