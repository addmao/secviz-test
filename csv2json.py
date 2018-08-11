#!/usr/bin/python
import re
import csv

with open('2018-07-Domestic Exchange - Index.csv') as domesticExchange:
	print "{"

	for line in domesticExchange:
		regex_pattern = re.match(r'(.*),(.*),(.*),(.*),(.*),(.*),(.*)', line)
	# print "{"

	# for line in data :
	# 	pattern = re.match(r'Plug#(\d+)\s\w+=(\d+\.\d+)\s\w+=(\d+\.\d+)\s\w+=(\d+\.\d+)\s\w+=(\d+\.\d+)\s\w+=(\d+\.\d+)\s\w+=(\d+\.\d+)', line)
	# 	#print line
		if regex_pattern:
			print " {"
			print "   " + " \"ASN-source\":\"" + regex_pattern.group(1) + "\","
			print "   " + " \"ASN\":\"" + regex_pattern.group(2) + "\","
			print "   " + " \"Name\":\"" + regex_pattern.group(3) + "\","
			print "   " + " \"Type\":\"" + regex_pattern.group(4) + "\","
			print "   " + " \"Bandwidth\":\"" + regex_pattern.group(5) + "\","
			print "   " + " \"Gb/s\":\"" + regex_pattern.group(6) + "\" ,"
			print "   " + " \"Connectivity Type\":\"" + regex_pattern.group(7) + "\""  #+ "\""
			print " }"
	# 		if(line[5] == '1' and line[6] == '2'):
	# 			print "  " + "}"
	# 		else :
	# 			print "  " + "},"
		else:
			print "No match!!"

	print "}"