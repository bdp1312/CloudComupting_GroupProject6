#!/usr/bin/env python3

import sys

current_word = None
current_count = 0
word = None

max_crime_boro = None
max_crime = 0

for line in sys.stdin:
	line = line.strip()
	
	word, count = line.split('\t', 1)

	try:
		count = int(count)
	except ValueError:
		continue
	
	if current_word == word:
		current_count += count
	else:
		if current_word:
			print("%s\t%s" % (current_word, current_count))
			if current_count > max_crime:
				max_crime = current_count
				max_crime_boro = current_word

		current_count = count
		current_word = word


if current_word == word:
	print("%s\t%s" % (current_word, current_count))

print("Max crime count is "+str(max_crime)+" in boro: "+str(max_crime_boro))
