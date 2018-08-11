#!/usr/bin/python
import re
import csv
from random import randint

with open('2018-07-Domestic Exchange - Index.csv') as domesticExchange:
	print "{"
	print " \"nodes\":\" ["

	for line in domesticExchange:
		regex_pattern = re.match(r'(.*),(.*),(.*),(.*),(.*),(.*),(.*)(\r+\s)', line)


		if regex_pattern:
			# print " {"
			#Node
			print "  {"
			print "    " + " \"color\": \"#c71934\","
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
	print "}"