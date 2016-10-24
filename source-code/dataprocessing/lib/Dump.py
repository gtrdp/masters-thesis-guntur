# this program dump the resulted data extraction to file
# (c) Guntur DP 2016 - guntur.dharma@gmail.com

from itertools import islice
import sys

class Dump:
	access_point = dict()
	probe_request = dict()
	audio_record = dict()
	ground_truth = dict()

	all_data = list()
	scan_date = ""

	def __init__(self, access_point, probe_request, audio_record, ground_truth, scan_date):
		self.access_point = access_point
		self.probe_request = probe_request
		self.audio_record = audio_record
		self.ground_truth = ground_truth
		self.scan_date = scan_date

	def readDump(self):
		# read all data from log file
		with open('data-dump.txt') as f:
			for line in islice(f, 3, None): # skip the headers
				foo = line.split("	")
				# convert to int
				for i, val in enumerate(foo):
					foo[i] = int(foo[i].strip())

				self.all_data.append(tuple(foo))

	def writeDump(self):
		# read previous data
		self.readDump()

		# we assume that the length of all ap pr and audio are the same
		for location in self.access_point:
			# only proceed if the variable length is the same
			if len(self.access_point[location]['timely']) == len(self.probe_request[location]['timely']) == len(self.audio_record[location]['timely']):
				for i in range(0, len(self.access_point[location]['timely'])):
					ap = self.access_point[location]['timely'][i]
					pr = self.probe_request[location]['timely'][i]
					au = self.audio_record[location]['timely'][i]
					gt = self.ground_truth[location][i]

					self.all_data.append((ap, pr, au, gt))
			else:
				print 'ERROR: the length of the input variables are not the same'
				sys.exit()

		# remove duplicates using set
		self.all_data = list(set(self.all_data))

		# write data to the file, overwrite
		target = open('data-dump.txt', 'w')
		# header comes first
		header = "[WiFi and Probe request correlation data]\n\nAP	PR	Au	GT\n"
		target.write(header)

		for value in self.all_data:
			target.write(str(value[0]) + "\t" + str(value[1]) + "\t" + str(value[2]) + "\t" + str(value[3]) +"\n")

		target.close()

	def writeLocalDump(self):
		# This function writes: correlation dump, raw data, manufacturer
		local_dump = list()

		# we assume that the length of all ap pr and audio are the same
		for location in self.access_point:
			# =======================================
			# 1. write the dump for correlation graph
			# only proceed if the variable length is the same
			if len(self.access_point[location]['timely']) == len(self.probe_request[location]['timely']) == len(
					self.audio_record[location]['timely']):
				for i in range(0, len(self.access_point[location]['timely'])):
					ap = self.access_point[location]['timely'][i]
					pr = self.probe_request[location]['timely'][i]
					au = self.audio_record[location]['timely'][i]
					gt = self.ground_truth[location][i]

					local_dump.append((ap, pr, au, gt))
			else:
				print 'ERROR: the length of the input variables are not the same (write local dump)'
				sys.exit()

			# remove duplicates using set
			local_dump = list(set(local_dump))

			# write data to the file, overwrite
			target = open(location + '-' + self.scan_date + '-dump.txt', 'w')
			# header comes first
			header = "[WiFi and Probe request correlation data for " + location +"-"+self.scan_date+"]\n\nAP	PR	Au	GT\n"
			target.write(header)

			for value in local_dump:
				target.write(
					str(value[0]) + "\t" + str(value[1]) + "\t" + str(value[2]) + "\t" + str(value[3]) + "\n")

			# close the handle and empty the list
			target.close()
			local_dump = list()

			# ==========================
			# 2. the processed data dump
			target = open(location + '-' + self.scan_date + '-raw.txt', 'w')
			# header comes first
			header = "[Raw data for " + location + "-" + self.scan_date + "]\n\n"
			target.write(header)

			target.write("access point\n" + repr(self.access_point[location]) + "\n\n\n")
			target.write("probe request\n" + repr(self.probe_request[location]) + "\n\n\n")
			target.write("audio record\n" + repr(self.audio_record[location]) + "\n\n\n")
			target.write("ground truth\n" + repr(self.ground_truth[location]) + "\n\n\n")

			# close the handle and empty the list
			target.close()

			# ====================
			# 3. manufacturer dump
			# firstly read OUI list and store that in memory
			# for MAC address removal
			oui_list = dict()
			with open('nmap-mac-prefixes.txt') as f:
				for line in f:
					(macaddr, company) = line.split("	")
					oui_list[macaddr] = company

			# the file handler
			target = open(location + '-' + self.scan_date + '-manufacturer.txt', 'w')
			header = "[Manufacturer dump for " + location + "-" + self.scan_date + "]\n\n"
			target.write(header)

			# for access point
			ap_mac = dict()
			for idx, value in self.access_point[location]['total'].iteritems():
				foo = idx.upper().replace(':', '') # get the formatted mac address

				oui = foo[0:6]

				# check if the MAC address complies with IEEE OUI standards
				try:
					vendor = oui_list[oui].strip()
				except Exception, e:
					vendor = ""

				if vendor and vendor not in ap_mac:
					ap_mac[vendor] = 1
				elif vendor and vendor in ap_mac:
					ap_mac[vendor] = ap_mac[vendor] + 1

			# write to file
			target.write("access point\n")
			for idx, value in ap_mac.iteritems():
				target.write(idx + "\t" + str(value) + "\n")
			target.write("\n\n\n")

			# for probe request
			pr_mac = dict()
			for idx, value in self.probe_request[location]['total'].iteritems():
				oui = idx[0:6]

				# check if the MAC address complies with IEEE OUI standards
				try:
					vendor = oui_list[oui].strip()
				except Exception, e:
					vendor = "randomMAC"

				if vendor and vendor not in pr_mac:
					pr_mac[vendor] = 1
				elif vendor and vendor in pr_mac:
					pr_mac[vendor] = pr_mac[vendor] + 1

			# write to file
			target.write("probe request\n")
			for idx, value in pr_mac.iteritems():
				target.write(idx + "\t" + str(value) + "\n")

			target.close()
