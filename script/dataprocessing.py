#!/usr/bin/env python
# Data preprocessing script for wifi probe-request and access point
# These following packages are required:
# - scipy

# import matplotlib.pyplot as plt
import re, os

# plt.plot([1,2,3,4], [1,4,9,16])
# plt.axis([0, 6, 0, 20])
# plt.show()

access_point = []
probe_request = []

# the access point file
# split the columns using regex
for filename in os.listdir("data/"):
    if len(filename.split("-")) == 4:
    	# print filename
    	(location, scan_type, scan_date, scan_time) = filename.split("-")
    	if scan_type == "ap" :
    		# access point
			d = []
			with open("data/" + filename) as f:
			    for line in f:
					ssid = ""
					bssid = ""
					rssi = ""
					regex = r'(.*) ([a-z|0-9]{2}:[a-z|0-9]{2}:[a-z|0-9]{2}:[a-z|0-9]{2}:[a-z|0-9]{2}:[a-z|0-9]{2}) (-[0-9]* )'
					
					# get the bssid
					matches = re.search(regex, line)
					if matches:
						bssid = matches.group(2)
					# get the ssid (name)
					matches = re.match(regex, line)
					if matches:
						ssid = matches.group(1).strip()
					# get the signal strength
					matches = re.match(regex, line)
					if matches:
						rssi = matches.group(3)

					# append that to the list
					if bssid and ssid and rssi:
						d.append({'bssid': bssid, 'ssid': ssid, 'rssi': rssi})
					# write to file (if needed)

			print d

# the probe request file

# from the dictionary, generate the graph
