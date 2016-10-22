# this program dump the resulted data extraction to file
# (c) Guntur DP 2016 - guntur.dharma@gmail.com

from itertools import islice
import sys

class Dump:
	access_point = dict()
	probe_request = dict()
	audio_record = dict()

	all_data = list()

	def __init__(self, access_point, probe_request, audio_record):
		self.access_point = access_point
		self.probe_request = probe_request
		self.audio_record = audio_record

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

					self.all_data.append((ap, pr, au))
			else:
				print 'ERROR: the length of the input variables are not the same'
				sys.exit()

		# remove duplicates using set
		self.all_data = list(set(self.all_data))

		# write data to the file, overwrite
		target = open('data-dump.txt', 'w')
		# header comes first
		header = "[WiFi and Probe request correlation data]\n\nAP	PR	Audio\n"
		target.write(header)

		for value in self.all_data:
			target.write(str(value[0]) + "\t" + str(value[1]) + "\t" + str(value[2]) + "\n")

		target.close()