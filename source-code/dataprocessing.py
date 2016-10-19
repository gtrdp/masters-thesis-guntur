#!/usr/bin/env python
# Data preprocessing script for wifi probe-request and access point
# These following packages are required:
# - scipy
# 
# TODO
# - [x] incorporate speech count: using crowdpp
# - [x] make it runnable.
# - [x] create how to if it does not have sufficient input arguments.
# - [x] ready to set the cut off (threshold)
# - [x] fix the legend location.
# - [x] apply MAC address OUI removal and show the graph.
# - [ ] create text data dump for scatter plot.
# - [ ] create dump file for each location for each date
# - [ ] restructure the code to make it modular
# - [ ] create vendor comparison from dump file.
# - [ ] incorporate rssi for access point.
#
# LG nexus MAC address: 78:f8:82:ca:98:2a

import matplotlib.pyplot as plt
import re, os
from collections import Counter
from itertools import chain
import pprint
from matplotlib.backends.backend_pdf import PdfPages
import subprocess
import sys

access_point = dict()
probe_request = dict()
audio_record = dict()
oui_list = dict()
pp = pprint.PrettyPrinter(indent=4)

# Check the input arguments
if len(sys.argv) == 4:
	threshold = int(sys.argv[1])
	mac_remove = int(sys.argv[2])
	audio = int(sys.argv[3])
else:
	print "3 arguments needed: threshold, MAC address removal, audio processing"
	print "Example: ./dataprocessing.py 5 1 1"
	print "Means: treshold:5, MAC address removal: yes, audio processing: yes"
	sys.exit()

# firstly read OUI list and store that in memory
# for MAC address removal
with open('nmap-mac-prefixes.txt') as f:
	for line in f:
		(macaddr, company) = line.split("	")
		oui_list[macaddr] = company

# the access point file
# split the columns using regex
for filename in os.listdir("data/"):
	if len(filename.split("-")) == 4:
		# get the parameters from filename
		(location, scan_type, scan_date, scan_time) = filename.split("-")
		
		# access point
		if scan_type == "ap" : 
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
					# beware of doubled mac addresses
					if bssid and ssid: #and rssi:
						foo.append({'bssid': bssid, 'ssid': ssid}) #, 'rssi': rssi})
			
			if location not in access_point:
				# new record
				access_point[location] = {'total': foo, 'timely': [len(foo)]}
			else:
				access_point[location]['total'].extend(foo)
				access_point[location]['timely'].append(len(foo))

		# probe request log
		elif scan_type == "pr":
			foo = dict()
			
			scan_time = scan_time[:-4]

			with open("data/" + filename) as f:
			    for line in f:
					macaddr = ""
					regex = r'SA:[a-z|0-9]{2}:[a-z|0-9]{2}:[a-z|0-9]{2}:[a-z|0-9]{2}:[a-z|0-9]{2}:[a-z|0-9]{2}'
					
					# get the macaddr
					matches = re.search(regex, line)
					if matches:
						macaddr = matches.group()[3:17].upper().replace(':', '')
						oui = macaddr[0:6]

						# if mac address filter is set, remove those mac address who is not on the OUI list
						try:
							vendor = oui_list[oui].strip()
						except Exception, e:
							vendor = ""

						# check if the MAC address complies with IEEE OUI standards
						if vendor and mac_remove:
							# remove the
							macaddr = macaddr.replace(oui,vendor + ':')
							# print macaddr
						elif mac_remove:
							macaddr = ""

					# append that to the dictionary
					if macaddr:
						if macaddr not in foo:
							foo[macaddr] = 1
						else:
							foo[macaddr] = foo[macaddr] + 1
			
			# data removal
			if threshold > 0:
				# remove insignificant mac address
				for row in list(foo) :
					if foo[row] < threshold:
						foo.pop(row, None)

			if location not in probe_request:
				# new record
				probe_request[location] = {'total': foo, 'timely': [len(foo)]}
			else:
				probe_request[location]['total'] = foo
				probe_request[location]['timely'].append(len(foo))

		elif scan_type == "au" and audio: # audio files
			# run the jar file
			foo = subprocess.check_output(['java', '-jar', 'speakercount-ready.old.jar', 'data/'+filename])
			foo = foo.strip()

			try:
				foo_int = int(foo)
			except Exception, e:
				foo_int = 0

			if location not in audio_record:
				# new record
				audio_record[location] = {'total' : foo_int, 'timely': [foo_int]}
			else:
				audio_record[location]['total'] += foo_int
				audio_record[location]['timely'].append(foo_int)
		# end if

# dump the result in a local log file

# dump the result in data dump file
# remove duplicate data first
with open('data-dump.txt') as f:
	for line in f:
		ap_count = []
		pr_count = []


# show up the result
for location in access_point:
	print location
	pp.pprint(access_point[location]['timely'])
	pp.pprint(probe_request[location]['timely'])
	if audio:
		pp.pprint(audio_record[location]['timely'])

	# prepare the figure
	plt.figure()
	plt.plot(access_point[location]['timely'], label='Access Point count')
	plt.plot(probe_request[location]['timely'], label='Unique devices')
	if audio:
		plt.plot(audio_record[location]['timely'], label='Speaker Count')
	plt.axis([0, 12.2, 0, max(probe_request[location]['timely']) + 50])
	plt.xlabel('Measurement')
	plt.ylabel('Number of MAC address')
	plt.title(location)

	# annotate the points
	for idx, value in enumerate(access_point[location]['timely']):
		plt.annotate(str(value), xy=(idx,value))
	for idx, value in enumerate(probe_request[location]['timely']):
		plt.annotate(str(value), xy=(idx,value))
	if audio:
		for idx, value in enumerate(audio_record[location]['timely']):
			plt.annotate(str(value), xy=(idx,value))
	lgd = plt.legend(bbox_to_anchor=(1, 1), loc='upper right', ncol=1)
    
    # plt.xticks(1)
	# pdfgraph = PdfPages(location + '-' + scan_date +'-after-'+threshold+'.pdf')
	# pdfgraph.savefig(plt.gcf())
	# pdfgraph.close()
	plt.show()

# plotting scatter table and calculating correlation
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats.stats import pearsonr

# n = 1024
# X = np.random.normal(0,1,n)
# Y = np.random.normal(0,1,n)

# print X
# print pearsonr(X,Y)

# plt.scatter(X,Y)
# plt.show()


# All result
# grotemarkt
# [27, 30, 25, 28]
# [1263, 1404, 2679, 3951]
# ikea
# [48, 53, 52, 49]
# [823, 928, 1567, 2098]

# After removal
# grotemarkt
# [27, 30, 25, 28]
# [39, 45, 64, 102]
# ikea
# [48, 53, 52, 49]
# [229, 238, 363, 455]