#!/usr/bin/python
import re
import csv
from random import randint

with open('2018-07-Domestic Exchange - Index.csv') as domesticExchange:
	print "{"
	print " \"nodes\": ["

	for line in domesticExchange:
		regex_pattern = re.match(r'(.*),(.*),(.*),(.*),(.*),(.*),(.*)(\r+\s)', line)
		# x = randint(0, 16777215)

		if regex_pattern:
			# print " {"
			#Node
			print "  {"
			print "    " + " \"color\": \"#" + str(hex(randint(0, 16777215)).split('x')[-1]) + "\","
			print "    " + " \"label\": \"" + regex_pattern.group(1) + "\","
			print "    " + " \"attributes\": {"
			print "      },"
			print "    " + " \"y\": " +  str(randint(1, 100)) + ","
			print "    " + " \"x\": " +  str(randint(1, 100)) + ","
			print "    " + " \"id\": \"" + regex_pattern.group(1) + "\","
			print "    " + " \"size\": " + regex_pattern.group(5) + ","
			print "  },"

		# else:
		#  	print "No match!!"
	print " ],"

with open('2018-07-Domestic Exchange - Index.csv') as domesticExchange:

	print " \"edges\": ["

	for line1 in domesticExchange:
		regex_pattern = re.match(r'(.*),(.*),(.*),(.*),(.*),(.*),(.*)(\r+\s)', line1)
		# x = randint(0, 16777215)

		if regex_pattern:
			# print " {"
			#Edge
			print "  {"
			print "    " + " \"sourceID\": \"" + regex_pattern.group(1) + "\","
			print "    " + " \"attributes\": {"
			print "      },"
			print "    " + " \"targetID\": \"" + regex_pattern.group(2) + "\","
			print "    " + " \"size\": " + str(1) + ","
			print "  },"
		# else:
		#  	print "No match!!"
	print " ],"
	print "}"