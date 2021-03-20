#!/usr/bin/env python3

from csv import reader
import sys

# Skip header of CSV file
next(sys.stdin)

crimeCount = {}

for line in reader(sys.stdin):
	boro, crime = (line[13].strip(), line[7].strip())
	
	if not boro or not crime:
		continue
	
	#Increment how many crimes were committed in the given boro
	if boro not in crimeCount:
		crimeCount[boro] = 1
	else:
		crimeCount[boro] += 1
	
#Output the total for each boro to the reducer task
for key in crimeCount:
	print("%s\t%s" % (key, crimeCount[key]))
