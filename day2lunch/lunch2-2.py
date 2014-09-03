#!/usr/bin/env python

#Counts number of perfectly matched alignments
f = open("/Users/cmdb/data/day2/accepted_hits.sam")
counter = 0

for line in f:
    if "HO" in line: #SAM tag for criteria
        counter = counter + 1
print counter