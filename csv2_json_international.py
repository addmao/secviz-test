#!/usr/bin/python
import re
from random import randint

unique_id = []

def NotDuplicate(regex_pattern):
	if regex_pattern not in unique_id:
		unique_id.append(regex_pattern)
		return True
	
	else:
		return False

#Node
with open('2018-07-International Exchange - _Index.csv') as interExchange:
	print "{"
	print " \"nodes\": ["

	for line in interExchange:
		regex_pattern = re.match(r'(.*),(.*),(.*),(.*),(.*),(.*),(.*)\n', line)
		regex_end = re.match(r'(.*),(.*),(.*),(.*),(.*),(.*),(.*)\Z', line)


		if regex_pattern:				
			if NotDuplicate(regex_pattern.group(1)) and regex_pattern.group(1) != 'AS38794': #find needle...
				print "  {"
				print "    " + " \"color\": \"#" + str(hex(randint(0, 16777215)).split('x')[-1]) + "\","
				print "    " + " \"label\": \"" + (regex_pattern.group(1)) + "\","
				print "    " + " \"attributes\": {"
				print "      },"
				print "    " + " \"y\": " +  str(randint(1, 100)) + ","
				print "    " + " \"x\": " +  str(randint(1, 100)) + ","
				print "    " + " \"id\": \"" + (regex_pattern.group(1)) + "\","
				print "    " + " \"size\": " + str(int(regex_pattern.group(5)) / 10)
				print "  },"

		if regex_end:
			# if NotDuplicate(regex_end.group(1)):
				print "  {"
				print "    " + " \"color\": \"#" + str(hex(randint(0, 16777215)).split('x')[-1]) + "\","
				print "    " + " \"label\": \"" + (regex_end.group(1)) + "\","
				print "    " + " \"attributes\": {"
				print "      },"
				print "    " + " \"y\": " +  str(randint(1, 100)) + ","
				print "    " + " \"x\": " +  str(randint(1, 100)) + ","
				print "    " + " \"id\": \"" + (regex_end.group(1)) + "\","
				print "    " + " \"size\": " + regex_end.group(5)
				print "  }"
	print " ],"

with open('2018-07-International Exchange - _Index.csv') as interExchange:

	print " \"edges\": ["

	for line1 in interExchange:
		regex_pattern = re.match(r'(.*),(.*),(.*),(.*),(.*),(.*),(.*)\n', line1)
		regex_end = re.match(r'(.*),(.*),(.*),(.*),(.*),(.*),(.*)\Z', line1)

		if regex_pattern:
			# print " {"
			#Edge
			print "  {"
			print "    " + " \"sourceID\": \"" + regex_pattern.group(1) + "\","
			print "    " + " \"attributes\": {"
			print " "
			print "      },"
			print "    " + " \"targetID\": \"" + regex_pattern.group(2) + "\","
			print "    " + " \"size\": " + str(1)
			print "  },"

	 	if regex_end:
	 		print "  {"
			print "    " + " \"sourceID\": \"" + regex_end.group(1) + "\","
			print "    " + " \"attributes\": {"
			print " "
			print "      },"
			print "    " + " \"targetID\": \"" + regex_end.group(2) + "\","
			print "    " + " \"size\": " + str(1)
	 		print "  }"
		# else:
		#  	print "No match!!"
	print " ]"
	print "}"