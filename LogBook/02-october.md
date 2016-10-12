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
		- Remove unrelated code block, such as the relation with smartphone things: battery, calibration (because we do not use semisupervised learning based on the owner voice) etc.
		- The code also uses Java Speech Toolkit (JSTK) from Speech Group at Informatik 5, Univ. Erlangen-Nuremberg, GERMANY.
			- https://github.com/sikoried/jstk
		- Most time spent on debugging the code.
		- Crowdpp also uses YIN pitch tracking algorithm: http://recherche.ircam.fr/equipes/pcm/cheveign/ps/2002_JASA_YIN_proof.pdf
		- Finally got the code to work, bug found in file format and feature extraction (delete the feature after completed, otherwise the next process will append it which will cause Exception)
		- Result on IKEA (the audio must be converted to wav first), which may be wrong (no ground truth available):
			```
			SpeakerCountTask: Finish YIN
			MFCC: audio/ikea.wav.mfcc.bin audio/ikea.wav.jstk.mfcc.txt
			SpeakerCountTask: Finish MFCC
			Speaker count: 2376
			```
		- Result on Grotemarkt:
			```
			SpeakerCountTask: Finish YIN
			MFCC: audio/grotemarkt.wav.mfcc.bin audio/grotemarkt.wav.jstk.mfcc.txt
			SpeakerCountTask: Finish MFCC
			Speaker count: 1702
			```

	- **Argument**: picture based ground truth has a problem in very dymanic places, e.g., grotemarkt.
	- Found SoX, an audio recorder (and even more) for sound recording: http://sox.sourceforge.net/sox.html
		- To record an 5 minutes wav (32 bit PCM) audio (better to down sample the quality, e.g., 16 bit PCM):
		```
		sox -d coba.wav trim 0 05:00
		```
	- **For Presentation** Explain that scanning AP and probe request is impossible to be carried out simultaneously, due to the different WiFi mode.

- **Fri Oct  7 10:02:12 CEST 2016**
	- [x] Revising thesis.
	- [x] Fixing the code for saturday experiment.
	- [x] Looking for bluetooth in terminal: it seems impossible as no solution found.
		- Better to do that in phone, and log the result.
		- using swift: http://stackoverflow.com/questions/24321126/get-bluetooth-devices-in-range-with-swift
		- could not find a reliable solution for mac os.
	- [x] Helping to fix the SME problem.
	- Look for how to build matlab code to be executable.
	- For a very dense crowd, look for an event.
	- **Research** possible problem: moving people, because it is simply hard to track.
		- **Focus** Possibly one place at different time, say grote markt, IKEA, campus.
			- Padeppoel: http://www.inwinkelcentra.nl/winkelcentrum-paddepoel/
			- Grote markt: https://gemeente.groningen.nl/sites/default/files/16-evenementenprofiel-grote-markt-br-a4-cw-maart.pdf
			- Grote markt: https://www.rug.nl/staff/p.h.pellenbarg/voordrachten/19._groningen_en_de_grote_markt_haalbaarheid_en_kwaliteit.pdf
			- Vismarkt: https://gemeente.groningen.nl/sites/default/files/16-evenementenprofiel-vismarkt-br-a4-rh-0104.pdf
			- IKEA (see page 7 and 9) http://www.ruimtelijkeplannen.nl/documents/NL.IMRO.0848.BP701ekkersrijt-OH01/tb_NL.IMRO.0848.BP701ekkersrijt-OH01_02.pdf
			- P.S. the above documents have also been saved locally for backup if the link broke.
	- Trying other VAD libraries.
		- https://pypi.python.org/pypi/webrtcvad
		- The `crowdpp` does not seem to be really accurate.

- **Sat Oct  8 12:04:35 CEST 2016**
	- Experiment for both social density and mac address randomization.
	- **Possible experimental setup**
		- set a table of experiment. do the same place for several consecutive days.
		- mark the only 1 probe request as passing by people.
	- **Tips**:
		- If you feel so tired, relax, take a deep sleep and tomorrow morning you'll get better and more energetic.
		- Read news, which is good to open up conversation with supervisors.
	- Interesting for randomization: http://www.slideshare.net/airtight/ios8-mac-randomization-via-airtight-blog-series
	- Learning about MAC address randomization.

- **Sun**
	- Deadline Chapter 2.
	- [ ] create preprocessing script ready for production.
		- [x] incorporate speech count: using crowdpp
		- [x] make it runnable.
		- [x] create how to if it does not have sufficient input arguments.
		- [x] ready to set the cut off (threshold)
		- [x] fix the legend location.
		- [ ] apply MAC address OUI removal and show the graph.
		- [ ] create text data dump for scatter plot.
	- [x] Fixing sensing app.
		- [x] Add number of loop, so that the script will stop when it reaches this number.
		- [x] Add sleep time.

October #2
----------
- **Mon Oct 10 11:52:51 CEST 2016**
	- Prepare the presentation for friday.
		- How to count correlation: Pearson r.
			- And explain about what it does.
			- Possibly look for other methods of getting correlation. 
		- Do the experiment twice, with different scanning period.
		- Explaing the scanning mechanism, what we do in each scanning period.
		- set a table of experiment. do the same place for several consecutive days.
		- show the correlation scatter graph, as found somewhere near sk-learn.
		- explain the instruments used: tech spech of macbook air.
	- Email Niels.
	- Beware of winter break, as everyone is going to be away for vacation.
		- Preferably to have the thesis done before winter break, as in january Prof Aiello is also gonna be away for sabbatical leave.
	- Studying for Nederlandse toetsen.
	- Answering SME questions.

- **Tue Oct 11 11:01:34 CEST 2016**
	- Working on presentation for Friday.
	- Working on SME.
	- **Possible ideas** For other location, use wiggle.net as the basis of selection.
	- Making the script executable. Creating quite mode for the java code.
	- Working on the `wifisense.sh` and `dataprocessing.py`
	- Looking for the difference between `adhoc` and `infrastructure` wifi.
	- Got the OUI list here: http://linuxnet.ca/ieee/oui/
		- The OUI part is almost done.

- **Wed Oct 12 10:30:13 CEST 2016**
	- Call Niels.
		- Explain about machine learning (with 3 features) approach.
		- Make presentation, that will also be presented on Friday.
		- Does behapp also scan for BLE device? or only classic bluetooth?
		- How big is the required N?
	- **Discussion notes**:
		- Forget about Bluetooth, as it is proven to be unstable. Although bluetooth is on, it is not discoverable.
		- How big is the N? is a magic question, it really depends on the data. The thing is, the data should give a firm insight of understanding.
		- VAD and speaker count are promising, learn how it works.
		- In Crowdpp `theta_s` and `theta_d` are the parameters for detecting speaker count. Play with it.
		- Do the scanning in this patern: 1 minute probe request and AP scanning. That way we might avoid the randomization and we can get more data points.
		- For a short experiment, compare the result of 1 minute, 5 and 10 minutes, and see whether there is a linear correlation (increase).
		- Test and recheck what Freudiger has done about MAC address randomization.
		- When android is in energy saving mode, the OS prohibits any app for doing WiFi Scan or any other scan.
		- See how often randomization occurs, and how often phone sends out probe request.
	- Bluetooth has 10 meters of range: http://www.sans.edu/research/security-laboratory/article/bluetooth
	- BLE scanner in Mac: https://github.com/samuraipapa/BLE-Mac-Scanner
	- Do MAC address randomization experiment tonight.

- **Thu**
	- 

- **Fri**
	- Meeting with Prof Aiello and Prof Kas.
		- Prepare the schedule for the next meeting.
		- Possible ground truth is official document from stakeholders.
		- How big is the required N?
		- It is also useless if we use very good microphone, as we will eventually implement that in a simple microphone on smartphone.
		- How if we do not have enough data?
		- Is the method scientifically correct?
	- Listing the lecturers for email.


October #3
----------
While doing data collection, also work with writing the thesis or reading the book.

October #4
----------