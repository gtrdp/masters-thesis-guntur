# this program read the condensed log file and plot it in a graph
# (c) Guntur DP 2016 - guntur.dharma@gmail.com

import matplotlib.pyplot as plt
import pprint
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr
from itertools import islice

class PlotGraph:
	pp = pprint.PrettyPrinter(indent=4)
	access_point = dict()
	probe_request = dict()
	audio_record = dict()
	ground_truth = dict()

	audio = 0
	scan_date = ""
	threshold = 0

	def __init__(self, access_point, probe_request, audio_record, ground_truth, audio, scan_date, threshold):
		self.access_point = access_point
		self.probe_request = probe_request
		self.audio_record = audio_record
		self.ground_truth = ground_truth

		self.audio = audio
		self.scan_date = scan_date
		self.threshold = threshold

	def plot(self):
		for location in self.access_point:
			# prepare the figure
			plt.figure(1)
			plt.plot(self.access_point[location]['timely'], label='Access Point count')
			plt.plot(self.probe_request[location]['timely'], label='Unique devices')
			if self.audio:
				plt.plot(self.audio_record[location]['timely'], label='Speaker Count')
			plt.plot(self.ground_truth[location], label='Ground Truth')

			max_x = len(self.access_point[location]['timely']) + 0.2
			max_y = max(self.probe_request[location]['timely'] + self.access_point[location]['timely'] + self.ground_truth[location])
			print max_y
			plt.axis([0, max_x, 0, max_y + int(round(0.25*max_y))])
			plt.xlabel('Measurement')
			plt.ylabel('Parameters')
			plt.title(location)

			# annotate the points
			for idx, value in enumerate(self.access_point[location]['timely']):
				plt.annotate(str(value), xy=(idx, value))
			for idx, value in enumerate(self.probe_request[location]['timely']):
				plt.annotate(str(value), xy=(idx, value))
			if self.audio:
				for idx, value in enumerate(self.audio_record[location]['timely']):
					plt.annotate(str(value), xy=(idx, value))
			for idx, value in enumerate(self.ground_truth[location]):
				plt.annotate(str(value), xy=(idx, value))

			lgd = plt.legend(bbox_to_anchor=(1, 1), loc='upper right', ncol=1)

			# plt.xticks(1)
			pdfgraph = PdfPages(location + '-' + self.scan_date +'-after-'+ str(self.threshold) +'.pdf')
			pdfgraph.savefig(plt.gcf())
			pdfgraph.close()
			# plt.show()

			print "The graph is saved..."

			# plot scatter and count the correlation

	def plotScatter(self, ap, pr, au, gt, location):
		# plotting scatter table and calculating correlation
		# ap vs. pr
		plt.figure(2)
		plt.xlabel('Unique Device (Probe request)')
		plt.ylabel('Access Point count')
		plt.title(location)
		plt.scatter(pr, ap)

		if location == "global":
			pdfgraph = PdfPages(location + '-pr-vs-ap.pdf')
		else:
			pdfgraph = PdfPages(location + '-' + self.scan_date + '-pr-vs-ap.pdf')

		pdfgraph.savefig(plt.gcf())
		pdfgraph.close()

		print location + " - ap vs. pr: " + str(pearsonr(pr, ap))

		# pr vs. gt
		plt.figure(3)
		plt.xlabel('Unique Device (Probe request)')
		plt.ylabel('Ground Truth')
		plt.title(location)
		plt.scatter(pr, gt)

		if location == "global":
			pdfgraph = PdfPages(location + '-pr-vs-gt.pdf')
		else:
			pdfgraph = PdfPages(location + '-' + self.scan_date + '-pr-vs-gt.pdf')

		pdfgraph.savefig(plt.gcf())
		pdfgraph.close()

		print location + " - pr vs. gt: " + str(
			pearsonr(pr, gt))

		# gt vs. ap
		plt.figure(4)
		plt.xlabel('Ground truth')
		plt.ylabel('Access Point count')
		plt.title(location)
		plt.scatter(gt, ap)

		if location == "global":
			pdfgraph = PdfPages(location + '-gt-vs-ap.pdf')
		else:
			pdfgraph = PdfPages(location + '-' + self.scan_date + '-gt-vs-ap.pdf')

		pdfgraph.savefig(plt.gcf())
		pdfgraph.close()

		print location + " - gt vs. ap: " + str(
			pearsonr(gt, ap))

	def plotScatterGlobal(self):
		ap = list()
		pr = list()
		au = list()
		gt = list()

		# read all data from log file
		with open('data-dump.txt') as f:
			for line in islice(f, 3, None):  # skip the headers
				foo = line.split("	")

				ap.append(int(foo[0].strip()))
				pr.append(int(foo[1].strip()))
				au.append(int(foo[2].strip()))
				gt.append(int(foo[3].strip()))

		self.plotScatter(ap, pr, au, gt, "global")

	def plotScatterLocal(self):
		for location in self.access_point:
			self.plotScatter(self.access_point[location]['timely'],
							 self.probe_request[location]['timely'],
							 self.audio_record[location]['timely'],
							 self.ground_truth[location],
							 location)
