#!/usr/bin/env python
#Counts number of alignments

f = open("/Users/cmdb/data/day2/accepted_hits.sam")

#Counts number of alignments
#header has already been removed
counter = 0
for line in f:
    if "SRR" in line:
        counter = counter + 1
print counter