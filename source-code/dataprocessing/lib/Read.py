# This program read the log file and save it to another condensed format
# (c) Guntur DP 2016 - guntur.dharma@gmail.com

import os, re
import subprocess

class Read:
	access_point = dict()
	probe_request = dict()
	audio_record = dict()
	decibel_sound = dict()
	ground_truth = dict()
	oui_list = dict()

	threshold = 0
	mac_remove = 0
	audio = 0

	def __init__(self, threshold, mac_remove, audio):
		self.threshold = threshold
		self.mac_remove = mac_remove
		self.audio = audio

	def readLog(self):
		# firstly read OUI list and store that in memory
		# for MAC address removal
		with open('nmap-mac-prefixes.txt') as f:
			for line in f:
				(macaddr, company) = line.split("	")
				self.oui_list[macaddr] = company

		# the access point file
		# split the columns using regex
		for filename in os.listdir("data/"):
			if len(filename.split("-")) == 4:
				# get the parameters from filename
				(location, scan_type, scan_date, scan_time) = filename.split("-")

				# access point
				if scan_type == "ap":
					self.countAccessPoint(filename, scan_time, location)
				# probe request log
				elif scan_type == "pr":
					self.countProbe(filename, scan_time, location)
				# audio recording
				elif scan_type == "au" and self.audio:  # audio files
					self.countVoice(filename, scan_time, location)
				# ground truth data
				elif scan_type == "gt":
					self.groundTruthChecking(filename, scan_time, location)

		# return the result
		return self.access_point, self.probe_request, self.audio_record, self.ground_truth, scan_date

	def countProbe(self, filename, scan_time, location):
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
						vendor = self.oui_list[oui].strip()
					except Exception, e:
						vendor = ""

					# check if the MAC address complies with IEEE OUI standards
					if vendor and self.mac_remove:
						# remove the
						macaddr = macaddr.replace(oui, vendor + ':')
					# print macaddr
					elif self.mac_remove:
						macaddr = ""

				# append that to the dictionary
				if macaddr:
					if macaddr not in foo:
						foo[macaddr] = 1
					else:
						foo[macaddr] = foo[macaddr] + 1

		# data removal
		if self.threshold > 0:
			# remove insignificant mac address
			for row in list(foo):
				if foo[row] < self.threshold:
					foo.pop(row, None)

		if location not in self.probe_request:
			# new record
			self.probe_request[location] = {'total': foo, 'timely': [len(foo)]}
		else:
			self.probe_request[location]['total'] = foo
			self.probe_request[location]['timely'].append(len(foo))

	def countAccessPoint(self, filename, scan_time, location):
		ap_bssid = dict()
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
				if bssid and ssid:  # and rssi:
					# check if already in a list
					if bssid not in ap_bssid:
						ap_bssid[bssid] = ssid

		if location not in self.access_point:
			# new record
			self.access_point[location] = {'total': ap_bssid, 'timely': [len(ap_bssid)]}
		else:
			self.access_point[location]['total'].update(ap_bssid)
			self.access_point[location]['timely'].append(len(ap_bssid))

	def countVoice(self, filename, scan_time, location):
		# run the jar file
		foo = subprocess.check_output(['java', '-jar', 'speakercount-ready.old.jar', 'data/' + filename])
		foo = foo.strip()

		try:
			foo_int = int(foo)
		except Exception, e:
			foo_int = 0

		if location not in self.audio_record:
			# new record
			self.audio_record[location] = {'total': foo_int, 'timely': [foo_int]}
		else:
			self.audio_record[location]['total'] += foo_int
			self.audio_record[location]['timely'].append(foo_int)
			# end if

	def groundTruthChecking(self, filename, scan_time, location):
		self.ground_truth[location] = list()
		with open("data/" + filename) as f:
			for line in f:
				self.ground_truth[location].append(int(line.strip()))
