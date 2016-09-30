#!/bin/bash
# script to automate capturing wifi probe request and available accesspoint

# How it works
# 0. read the location name from the arguments
# 1. capture wifi probe-request packets for scan_duration minutes, save it to dump file
#    with current timestamp
# 2. kill the script to stop capturing the probe-request packets
# 3. start counting the available accesspoint and save it to a file with
#    current timestamp
# 4. repeat step 1 to 3 until the program receives SIG kill
#
# PS. always output what is happening now, and give current timestamp

# read location arguments
if [ $# -eq 0 ]
	then
		echo ""
		echo "No arguments supplied. Exiting..."
		echo ""
		# exit
		exit 1
	else
		location_name=$1
fi

loop=1
# main loop
while true; do
	echo ""
	echo "===============Loop: "$loop"==============="
	# capture probe request packets in background
	# prepare the file name
	file_name=$location_name-probe-request-$(date +%Y-%m-%d-%H.%M).txt
	echo ""
	echo "Capturing WiFi probe-request packets..."
	tcpdump -In -i en0 -e -s 256 type mgt subtype probe-req >> $file_name & 

	# wait for scan_duration
	sleep 60
	# kill the previous process
	echo ""
	echo "Killing the capturing process..."
	killall tcpdump inotifywait

	# logging available accesspoint
	# prepare the file name
	file_name=$location_name-access-point-$(date +%Y-%m-%d-%H.%M).txt
	echo ""
	echo "Logging available Access Point..."
	airport -s >> $file_name

	echo ""
	echo "Done."
	echo "Continue next loop..."
	loop=$((loop+1))
done
