#!/usr/bin/env python
# Data preprocessing script for wifi probe-request and access point
# 
# TODO
# - [x] create text data dump for scatter plot.
# - [x] create dump file for each location for each date
# - [x] restructure the code to make it modular
# - [x] create vendor comparison from dump file.
# - [x] incorporate ground truth
# - [ ] save the correlation result to txt file
# - [ ] filter out using rssi
# - [ ] also show the correlation value and p value in the graph
#
# LG nexus MAC address: 78:f8:82:ca:98:2a

import sys
from lib.Read import Read
from lib.Dump import Dump
from lib.PlotGraph import PlotGraph

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

# start reading the log
reader = Read(threshold,mac_remove,audio)
access_point, probe_request, audio_record, ground_truth, scan_date = reader.readLog()

# dump the result in a local log file
# for scatter plot
dumper = Dump(access_point, probe_request, audio_record, ground_truth, scan_date)
dumper.writeDump()
dumper.writeLocalDump()

# plot the result
plotter = PlotGraph(access_point, probe_request, audio_record, ground_truth, audio, scan_date, threshold)
plotter.plot()
plotter.plotScatterLocal()
plotter.plotScatterGlobal()
