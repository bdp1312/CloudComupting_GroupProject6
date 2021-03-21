#!/usr/bin/env python3

from csv import reader
import sys

# Skip header of CSV file
next(sys.stdin)

crime_count = {}
boro_crimes = {}

for line in reader(sys.stdin):
	boro, crime = (line[13].strip(), line[7].strip())
	
	if not boro or not crime:
		continue
	
	#Increment how many crimes were committed in the given boro
	if boro not in crime_count:
		crime_count[boro] = 1
	else:
		crime_count[boro] += 1
	
	#Make a list of all the crimes committed by boro
	if boro not in boro_crimes:
		boro_crimes[boro] = {crime} #New set if there is not already one
	else:
		boro_crimes[boro].add(crime) #Add to existing set of crimes otherwise


#Output the total for each boro to the reducer task
for key in crime_count:
	#Build the list of crimes for the current boro, separated by tabs
	crime_list = "\t".join(boro_crimes[key])
	print("%s\t%s\t%s" % (key, crime_count[key], crime_list))
