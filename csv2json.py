#!/usr/bin/python
import re
import csv

with open('2018-07-Domestic Exchange - Index.csv') as domesticExchange:
	print "{"

	for line in domesticExchange:
		regex_pattern = re.match(r'(.*),(.*),(.*),(.*),(.*),(.*),(.*)(\r+\s)', line)

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

		# else:
		# 	print "No match!!"

	print "}"