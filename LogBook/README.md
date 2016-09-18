Master's Thesis Log Book
============================
- Title: TBD
- First Supervisor: Prof. Marco Aiello
- Second Supervisor: Prof. Martien Kas
- Daily Supervisor: Niels Jongs
- Duration: September - January 2016
- Location: The University of Groningen, the Netherlands.

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
	- Another challenges: (i) using direct people count, (ii) using quantized counting level as proposed in some papers.
	- `[Possible problem]` A drawback of scanning WiFi probe request: people located in other room (not within the person's eyesight) is still detectable, thus, worsen the results.
	- Look for how to do a thesis in a proper way.
	- `[Possible novelty]` To filter the data, i.e., to remove laptops or other device, use known MAC address filter.
	- A device that scans for Wi-Fi or Bluetooth devices is available: Meshlium http://www.libelium.com/products/meshlium/

September #4
--------------------------------
- **Mon**
	- Prepare list of questions.
	- Check what to report for the SME TA.
- **Tue**
	- List of Questions:
		- one 
		- two
		- three
- **Wed**
- **Thu**
	- Make sure that you read the key literature (one which is similar) and make sure whether it contains proxy between social density and WiFi/BT signals.
- **Fri Aug 26 10:30:00 CEST 2016**
	- Literature Review Presentation.
September #5
--------------------------------

October #1
----------
