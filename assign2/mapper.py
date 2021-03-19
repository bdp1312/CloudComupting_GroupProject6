#!/usr/bin/env python3

from csv import reader
import sys

# Skip header of CSV file
next(sys.stdin)

for line in reader(sys.stdin):
	boro, crime = (line[13].strip(), line[7].strip())
	
	if not boro or not crime:
		continue

	#Rest of code
	#print("Boro: "+boro+", Crime: "+crime+"\n")
	# Map boro to trivial value of 1 for reducing later
	print("%s\t%s" % (boro, 1))
