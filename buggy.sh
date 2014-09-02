#!/bin/bash

#
# Day 1 - Homework: Part 2 - debug this bash script
#

echo "There are around 6 mistakes"

FASTQ_DIR=/Users/cmdb/data/fastq
OUTPUT_DIR=/Users/cmdb/data/day1
SAMPLE_PREFIX=SRR072

GENOME_DIR=/Users/cmdb/data/genomes
GENOME_PREFIX=dmel5
ANNOTATION=dmel-all-r5.57.gff

CORES=4

for i in {1..24}
do
  echo gunzip $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq.gz	
  echo fastqc $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq -o $OUTPUT_DIR
  echo tophat -p$CORES -G $OUTPUT_DIR/ANNOTATION -o tophat$i $GENOME_DIR/$GENOME_PREFIX $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq
  echo cufflinks -p$CORES -G $OUTPUT_DIR/ANNOTATION -o cufflinks_out tophat$i/accepted_hits.bam
done