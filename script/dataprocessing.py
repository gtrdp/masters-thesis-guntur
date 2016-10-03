#!/usr/bin/env python
# Data preprocessing script for wifi probe-request and access point
# These following packages are required:
# - scipy

import matplotlib.pyplot as plt
import re, os
from collections import Counter
from itertools import chain
import pprint

# plt.plot([1,2,3,4], [1,4,9,16])
# plt.axis([0, 6, 0, 20])
# plt.show()

access_point = dict()
probe_request = dict()

# the access point file
# split the columns using regex
for filename in os.listdir("data/"):
    if len(filename.split("-")) == 4:
    	# print filename
    	(location, scan_type, scan_date, scan_time) = filename.split("-")
    	if scan_type == "ap" :
    		# access point
			foo = []
			scan_time = scan_time[:-4]

			with open("data/" + filename) as f:
			    for line in f:
					ssid = ""
					bssid = ""
					# rssi = ""
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
					# matches = re.match(regex, line)
					# if matches:
					# 	rssi = matches.group(3)

					# append that to the list
					if bssid and ssid: #and rssi:
						foo.append({'bssid': bssid, 'ssid': ssid}) #, 'rssi': rssi})
			
			if location not in access_point:
				# new record
				access_point[location] = {'total': foo, 'timely': [len(foo)]}
			else:
				access_point[location]['total'].extend(foo)
				access_point[location]['timely'].append(len(foo))

			# print d

# show up the result
pp = pprint.PrettyPrinter(indent=4)
for location in access_point:
	print location
	pp.pprint(access_point[location]['timely'])
	
	plt.plot(access_point[location]['timely'])
	# plt.axis([0, 6, 0, 20])
	
plt.show()
# the probe request file

# from the dictionary, generate the graph
