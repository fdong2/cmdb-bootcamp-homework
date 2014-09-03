#!/usr/bin/env python

#Finds number of reads mapping to unique location

f = open("/Users/cmdb/data/day2/accepted_hits.sam")
counter = 0 

for line in f:
    if "NH:i" not in line: #checks if this optional criteria is present in file
        print "Invalid criteria"
        break
    if "NH:i:1" in line:
        counter = counter + 1
print counter
