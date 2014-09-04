#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

#Exercise 1

#find files
fly_1 = "/Users/cmdb/data/results/SRR072893_clout/genes.fpkm_tracking"
fly_2 = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"

#read files
df1 = pd.read_table(fly_1)
df2 = pd.read_table(fly_2)
third = 15602/3

#Sort and extract FPKM
df1_sorted = df1.sort("FPKM")["FPKM"]
df2_sorted = df2.sort("FPKM")["FPKM"]

#list contains top, middle, and lower third
df1_l = [ df1_sorted[ -third: ], df1_sorted[ third:-third ], df1_sorted[ 0:third ] ]
df2_l = [ df2_sorted[ -third: ], df2_sorted[ third:-third ], df2_sorted[ 0:third ] ]
tags = ["", "Top Third", "Middle Third", "Low Third", ""]

#Make plots
plt.figure(1)
plt.boxplot(df1_l)
plt.title("FPKM for SRR072893")
plt.xlabel("Portion of data")
plt.xticks(range(5), tags) #change x-axis ticks
plt.ylabel("FPKM")
plt.axis( [0, 4, 0, 200])
plt.savefig("SRR072893_box.png")

plt.figure(2)
plt.boxplot(df2_l)
plt.title("FPKM for SRR072915")
plt.xlabel("Portion of data")
plt.xticks(range(5), tags)
plt.ylabel("FPKM")
plt.axis( [0, 4, 0, 250])
plt.savefig("SRR072915_box.png")

#Exercises 2 and 3
#Exercises 2 and 3

#Locate and read metadata file
sample = pd.read_table("/Users/cmdb/data/day2/homework/samples.csv", sep=",")

#Get only females
sampfem = sample["sex"] == "female"
sample = sample[sampfem]

#Get only sxl and store FPKM
sxl_list = []
for fly in sample["sample"]:
    path = "/Users/cmdb/data/results/%s_clout/genes.fpkm_tracking" % fly
    data = pd.read_table(path)
    sxl = data["gene_short_name"] == "Sxl"
    lines_w_sxl = data[sxl]
    sxl_list.append(lines_w_sxl["FPKM"])

#Make plot
plt.figure(3)
plt.plot(sxl_list)
plt.title("Sxl in female development")
plt.xlabel("Stage")
plt.xticks(range(8), list(sample["stage"]))
plt.ylabel("FPKM")
plt.axis( [0, 7, 0, 400] )
plt.savefig("sxl.png")