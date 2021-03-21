#!/usr/bin/env python3

import sys

current_boro = None
current_count = 0
boro = None

max_crime_boro = None
max_crime = 0

boro_crimes = {}

for line in sys.stdin:
	line = line.strip()
	
	boro, count, crimes = line.split('\t', 2)

	try:
		count = int(count)
	except ValueError:
		continue
	
	
	if current_boro == boro:
		#Add the count to the running count for the current boro
		current_count += count
	else:
		#Otherwise, start counting for the next boro
		if current_boro:
			#Print out the stats for the current boro, then check for max
			print("%s\t%s" % (current_boro, current_count))
			if current_count > max_crime:
				max_crime = current_count
				max_crime_boro = current_boro
		#Start the count for the next boro
		current_count = count
		current_boro = boro
		#Make sure there's a set to hold the crimes for the current boro
		if current_boro not in boro_crimes:
			boro_crimes[current_boro] = set()
	
	if crimes:
		#Break up crimes, which are tab-separated
		for each_crime in crimes.split('\t'):
			#Add them to the list for the current_boro
			boro_crimes[current_boro].add(each_crime)


if current_boro == boro:
	print("%s\t%s" % (current_boro, current_count))

print("\nMax crime count is "+str(max_crime)+" in boro: "+str(max_crime_boro))
print("\nCrimes committed there:")

#Print the crimes committed in the boro with the most crimes
for crime in boro_crimes[max_crime_boro]:
	print(crime)
