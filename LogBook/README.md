Master's Thesis Log Book
============================
- Title: The Relation of Unique Number of Device and the Number of Available Access Points with the Validation of Ambient Noise
- First Supervisor: Prof. Marco Aiello
- Second Supervisor: Prof. Martien Kas
- Daily Supervisor: Niels Jongs
- Duration: September - January 2016
- Location: The University of Groningen, the Netherlands.

Timeline
--------
![alt tag](master-thesis-timeline.png)

August #2
---------
- **Tue Aug 9 13:00:00 CEST 2016**
	- Meeting with Prof. Kas and Niels Jongs.

August #4
---------
- **Fri Aug 26 09:30:00 CEST 2016**
	- Meeting with Prof. Kas.

September #1
------------
- **Fri Sep  2 13:00:00 CEST 2016**
	- Thesis meeting with Prof. Kas, Prof. Aiello, and Niels Jongs.


September #2 [Start Lit. Review]
--------------------------------
- **Mon Sep  5 16:37:08 CEST 2016**
	- Getting the master's template.
- **Tue Sep  6 09:38:10 CEST 2016**
	- Formatting the thesis template.
	- Start reviewing.
	- Creating excel file for the review summary.
	- Refactoring pdf references so that it has reference code.
- **Wed Sep  7 10:01:43 CEST 2016**
	- Reviewing thesis 008, 014, 012, 011, 017, 016.
	- **Question:** Is it possible to scan for probe requests in android device? It is possible in laptops.
	- For checking MAC address and manufacturer: Organizationally Unique Identifier.
	- Probably insert OUI graph in the report.
- **Thu Sep  8 11:16:42 CEST 2016**
	- Reading 016, 019, 015
- **Fri Sep  9 21:32:18 CEST 2016**
	- Printing lots of literatures.

September #3
--------------------------------
- **Mon Sep 12 12:04:21 CEST 2016**
	- Literature review.
	- Working on SME TA.
- **Tue Sep 13 10:15:14 CEST 2016**
	- Working on SME TA.
- **Wed Sep 14 10:16:12 CEST 2016**
	- Working on SME TA, in the morning.
	- Reading 026, 031, 030, 028, 020, 009
	- http://ohmage.org/ would be interesting to see. -> Looks like it is not updated anymore.
	- 031 seems to be very similar in methods. It reveals several interesting methods.
	- More WiFi literatures are needed.
	- Look for WiFi probe request in Android.
- **Thu Sep 15 09:29:49 CEST 2016**
	- Looking for and printing new literature.
	- Continue literature review: 001, 006, 040, 041
	- cannot find a literature that combines WiFi proxy and online signals (one uses probe request).
- **Fri Sep 16 11:28:14 CEST 2016**
	- Literature review: 041, 042, 043, 022
	- Learn about confision matrix, because some of the work use that.
	- I think it is hard to find a reliable source ground truth for our work.
	
- **Sat Sep 17 14:56:27 CEST 2016**
	- Continue Literature: 022, 033, 045
	- Getting `probe request` meaning makes the WiFi in monitoring mode (cannot be used as normal device for internet).
	- The problem is:
		- how to distinguish between people (represented by smartphone) and AP.
		- how to know that the person is within the eyesight of the person, because the WiFi probe request might be received but no human is in eyesight.
	- To be able to detect `probe request`, android must be set to `monitor mode`, which requires root privilege.
		- It also depends on the chipset of the Android, not all device supports `monitor mode`.
		- More read: http://stackoverflow.com/questions/2334244/is-there-any-way-to-put-android-wifi-droid-handset-into-promiscuous-monitoring
	- A good example: https://www.kismetwireless.net/android-pcap/
		- But it requires a USB NIC that supports `monitor mode`.
	- Bluetooth is only possible to count crowd, or estimates. Because it is counting only within 10% of real people count.
	- Rooting or jailbreaking is considered illegal in some countries: http://www.makeuseof.com/tag/illegal-root-android-jailbreak-iphone/
	- Look for possible other work that use `wifi probe request` in `thesis014`.
	- Look more about F-Measure.
	- Got many papers which seem relevant with crowd counting using probe request in WiFi.
	- Command to scan for probe request in Linux/Mac:

			sudo tcpdump -In -i en0 -e -s 256 type mgt subtype probe-req

- **Sun Sep 18 17:10:56 CEST 2016**
	- Continue literature: 047, 057
	- Look for how to calculate accuracy:
		- F-measure
		- R value (?)
		- correlation
	- Challenges, how to define the time of scanning. and figure out where to perform the scanning, which has a good spot (good point of view) for counting. Possible option:
		- Grotemarkt
		- Vismarkt
		- Academy gebouw
		- Bernoulliborg
		- Noorder plantsoen (with walking and recording video).
		- Duisenberg library
	- Another challenges: (i) using direct people count, (ii) using quantized counting level as proposed in some papers.
	- `[Possible problem]` A drawback of scanning WiFi probe request: people located in other room (not within the person's eyesight) is still detectable, thus, worsen the results.
		- Combine with sound
		- Combine with GPS location if there is no sound detected.
	- Look for how to do a thesis in a proper way.
	- `[Possible novelty]` To filter the data, i.e., to remove laptops or other device, use known MAC address filter.
	- A device that scans for Wi-Fi or Bluetooth devices is available: Meshlium http://www.libelium.com/products/meshlium/

September #4
--------------------------------
- **Mon Sep 19 09:41:44 CEST 2016**
	- Prepare list of questions.
	- Literature: 053, 060, 044, 051, 052, 058, 048
	- Possibly look for official WiFi technical specification from wifi.org.
	- `[Possible feature]` Filter based on RSSI. Find a literature that says the threshold of WiFi signal.
	- `[Possible challenges]` MAC randomization in iOS8 devices.
		- Possible ways, filtering: randomized MACs does not comply with IEEE standards [thesis053]
	- What is CDF?
	- Literature review searching:
		- Using several keywords
		- Getting the literature from bibliography of the paper
		- From author name, for possible other publication
	- `[Possible tips]` Please make sure that rooting an android phone is not breaking the law.
		- http://www.makeuseof.com/tag/illegal-root-android-jailbreak-iphone/
		- http://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=OJ:L:2009:111:0016:0022:EN:PDF
	- Bluetooth, WiFi and ambient sound, might be good candidates for objective social density measurement. 
	- `[Possible Method]` When measuring the WiFi packets (or any other source of data), please do that when the phone is
		- Inside the pocket, or bag.
		- Hold in the hand.
	- `[Suggestion]` Test the method firstly, by conducting a short-timed experiment, before going to the real experiment.
	- Also give graph of MAC address manufacturer.
	- Random question: Why WiFI can improve accuracy in smartphone location (as often asked when opening google maps)?


- **Tue Sep 20 09:46:59 CEST 2016**
	- Literature: 046
	- Attending Mas Tri's Seminar about Papua development.
	- Start writing summary of the literature review.
	- `[Possible idea]` Compare indoor and outdoor measurement.
	- List of Questions:
		- Is rooting an issue (illegal)? 
		- Is it better to have direct crowd count or using quantization?
		- Counting people using wifi has an issue: it can detect people through the walls, which people don't see. what do you think?

- **Wed Sep 21 10:10:26 CEST 2016**
	- Skype call with Niels. Some insights:
		- This work is going to be helpful for BeHapp app.
		- Try to find a correlation between probe request (proxy of people count), which indicates unique device and number of access point [novelty] in a particular area.
		- There is an issue with MAC address randomization, try to find a solution `probably solved in one of the paper`.
			- Possibly use a RSSI as a measurement.
		- If possible, also develop a model of wifi access point with the number of unique device.
			- So, if we have the access point count in BeHapp, we could infer the social density.
		- Got more literature.
	- Create simple presentation.
	- Devise a research proposal before meeting with Niels at 11.
	- Wisuda Didin.
	- Try to settle in one place until the end of the day. That way, you can save lot of time, rather than finding a place to stay.
	- Please be on time, in the morning, otherwise you will get no place to work.
	- Look for MAC address randomization.
	- `[Notice]` Becareful with WiFi channels, please scann all channels.
	- Interesing, for MAC address randomization in iOS.
	- `[Suggestions for Research]` Try to filter out other devices, e.g., tablets, or laptops, and see what happens.
	- `[Suggestions for Research]` Try to use different variable:
		- Location (classified in: remote area, crowded place, city center, indoor, outdoor)
		- Duration of scanning (15 mins, 30 mins, 45 mins)
		- Filter
		- Phone manufacturer
		- Operating System
		- number of sent probes per device
		- show the graph of scanned device (comparison between laptops, smartphones, and other)
	- Literature: 061
	- Both Android and iOS employ MAC address randomization.

- **Thu Sep 22 10:40:12 CEST 2016**
	- Make sure that you read the key literature (one which is similar) and make sure whether it contains proxy between social density and WiFi/BT signals.
	- Find how complicated is the other masters thesis.
		- Basically they have 1 to 3 research questions.
		- One is the main question, while several others are the subquestions.
	- Making the slides for tomorrow.
	- Keyword used for literature study:
		- `crowd counting wifi`
		- `crowd counting bluetooth`
		- `wifi probe request`
		- `online database social density`
		- `counting crowd`
		- `android monitor mode`
		- `probe request wifi people`
		- `crowd density wifi bluetooth`
		- `social density online data`
		- `crowd sensing wifi`
		- `objective social density wifi bluetooth`
		- `social density data`
		- `social density objective`
	- creating summary table
	- `[MAC Randomization]` Chekc whether the randomized MAC address is locally administered address: https://en.wikipedia.org/wiki/MAC_address
	- Example of dedidated WiFi scanning device:
		- CrossCompass by Acyclia

- **Fri Aug 26 10:30:00 CEST 2016**
	- Literature Review Presentation.
	- Questions:
		- Prof. Aiello is going to have a sabbatical leave starting in January, is that going to be a problem?
		- Do 
		- When is the starting date of this thesis?
		- Who is going to be the first and second supervisor?
		- Wifi Probes have an issue, it can detect people through the wall, while people can't.
		- Smartphone can not scan for probe request, unless it is rooted or jailbreaked, which is rather illegal.
	- Meeting with Prof Aiello, Prof Kas, and Niels.
	- Next step !!!:
		- Experimental Setup.
		- Make sure that chapter 2 is finished by the next meeting.
		- Read more literatures about
			- MAC address randomization
			- Sensing MAC address using probe request
			- Ambient noise library
	- Please plan the work for the next week.

- **Sun Sep 25 14:37:42 CEST 2016**
	- Explain experimental setup also by using images.
	- Reading how to write a better thesis.
	- `[Possible Research Ideas]` Take into account people moving in and out
		- Mean of people per time window, i.e., 15 mins
		- The number getting in and out

September #5
--------------------------------
- **Mon Sep 26 09:57:10 CEST 2016**
	- Looking for a library for sound ambience.
		- Keyword: Voice Activity Detection (VAD)
		- https://en.wikipedia.org/wiki/Voice_activity_detection
		- https://en.wikipedia.org/wiki/Talkspurt
		- https://en.wikipedia.org/wiki/Comfort_noise
	- Detect voice activity and measure the intensity (dB).
	- VAD is, I assume, used only when the voice is clearly heard. It is unknown whether the usage is also possible where crowd is present.
	- `[Possible experiment]` Also try to do **moving** experiment, using Raspberry with WiFi monitor.
	- Several libraries for voice activity detection:
		- https://github.com/mvansegbroeck/vad
		- https://github.com/pckben/vad
		- https://github.com/shunsukeaihara/vad_for_voip
		- https://github.com/kdavis-mozilla/vad.js
	- Experimental setup: https://www.reference.com/science/experimental-setup-science-1e292d23676da70

October #1
----------
