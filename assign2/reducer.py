#!/usr/bin/env python3

import sys

current_boro = None
current_count = 0
boro = None

max_crime_boro = None
max_crime = 0

for line in sys.stdin:
	line = line.strip()
	
	boro, count = line.split('\t', 1)

	try:
		count = int(count)
	except ValueError:
		continue
	
	if current_boro == boro:
		current_count += count
	else:
		if current_boro:
			print("%s\t%s" % (current_boro, current_count))
			if current_count > max_crime:
				max_crime = current_count
				max_crime_boro = current_boro

		current_count = count
		current_boro = boro


if current_boro == boro:
	print("%s\t%s" % (current_boro, current_count))

print("Max crime count is "+str(max_crime)+" in boro: "+str(max_crime_boro))
