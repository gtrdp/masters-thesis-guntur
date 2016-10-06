#!/usr/bin/env python
# Data preprocessing script for wifi probe-request and access point
# These following packages are required:
# - scipy
# 
# TODO
# - Filter using OUI

import matplotlib.pyplot as plt
import re, os
from collections import Counter
from itertools import chain
import pprint
from matplotlib.backends.backend_pdf import PdfPages

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
		elif scan_type == "pr": # probe request log
			foo = dict()
			
			scan_time = scan_time[:-4]

			with open("data/" + filename) as f:
			    for line in f:
					macaddr = ""
					regex = r'SA:[a-z|0-9]{2}:[a-z|0-9]{2}:[a-z|0-9]{2}:[a-z|0-9]{2}:[a-z|0-9]{2}:[a-z|0-9]{2}'
					
					# get the macaddr
					matches = re.search(regex, line)
					if matches:
						macaddr = matches.group()

					# append that to the dictionary
					if macaddr:
						if macaddr not in foo:
							foo[macaddr] = 1
						else:
							foo[macaddr] = foo[macaddr] + 1
			
			# remove insignificant mac address
			# for row in list(foo) :
			# 	if foo[row] < 10:
			# 		foo.pop(row, None)

			if location not in probe_request:
				# new record
				probe_request[location] = {'total': foo, 'timely': [len(foo)]}
			else:
				probe_request[location]['total'] = foo
				probe_request[location]['timely'].append(len(foo))

		# end if

# show up the result
pp = pprint.PrettyPrinter(indent=4)
for location in access_point:
	print location
	pp.pprint(access_point[location]['timely'])
	pp.pprint(probe_request[location]['timely'])

	plt.figure()
	plt.plot(access_point[location]['timely'], label='Access Point count')
	plt.plot(probe_request[location]['timely'], label='Unique devices')
	plt.axis([0, 3.2, 0, max(probe_request[location]['timely'])+10])
	plt.xlabel('Measurement')
	plt.ylabel('Number of MAC address')
	plt.title(location)
	# annotate the points
	for idx, value in enumerate(access_point[location]['timely']):
		plt.annotate(str(value), xy=(idx,value))
	for idx, value in enumerate(probe_request[location]['timely']):
		plt.annotate(str(value), xy=(idx,value))
	lgd = plt.legend(bbox_to_anchor=(1, 1), loc='upper left', ncol=1)
    
    # plt.xticks(1)
	pdfgraph = PdfPages(location + '-before.pdf')
	pdfgraph.savefig(plt.gcf())
	pdfgraph.close()
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