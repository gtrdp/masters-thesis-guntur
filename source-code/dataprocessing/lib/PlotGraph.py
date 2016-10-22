# this program read the condensed log file and plot it in a graph
# (c) Guntur DP 2016 - guntur.dharma@gmail.com

import matplotlib.pyplot as plt
import pprint
from matplotlib.backends.backend_pdf import PdfPages

class PlotGraph:
	pp = pprint.PrettyPrinter(indent=4)
	access_point = dict()
	probe_request = dict()
	audio_record = dict()
	audio = 0

	def __init__(self, access_point, probe_request, audio_record, audio):
		self.access_point = access_point
		self.probe_request = probe_request
		self.audio_record = audio_record
		self.audio = audio

	def plot(self):
		for location in self.access_point:
			# prepare the figure
			plt.figure()
			plt.plot(self.access_point[location]['timely'], label='Access Point count')
			plt.plot(self.probe_request[location]['timely'], label='Unique devices')
			if self.audio:
				plt.plot(self.audio_record[location]['timely'], label='Speaker Count')
			plt.axis([0, 12.2, 0, max(self.probe_request[location]['timely']) + 50])
			plt.xlabel('Measurement')
			plt.ylabel('Number of MAC address')
			plt.title(location)

			# annotate the points
			for idx, value in enumerate(self.access_point[location]['timely']):
				plt.annotate(str(value), xy=(idx, value))
			for idx, value in enumerate(self.probe_request[location]['timely']):
				plt.annotate(str(value), xy=(idx, value))
			if self.audio:
				for idx, value in enumerate(self.audio_record[location]['timely']):
					plt.annotate(str(value), xy=(idx, value))
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
