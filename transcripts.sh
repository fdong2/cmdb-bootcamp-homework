#!/bin/bash

DIR=/Users/cmdb/data
EXT=/day1/cufflinks_out


bedtools flank -i $DIR$EXT/transcripts.gtf -g $DIR$EXT/genome.sizes.txt -l 250 -r 0 > transcripts250new.gtf
bedtools flank -i $DIR$EXT/transcripts250new.txt -g $DIR$EXT/genome.sizes.txt -l 0 -r 500 > transcripts500new.gtf
bedtools getfasta -fi $DIR/genomes/dmel-all-chromosome-r5.57.fasta -bed $DIR$EXT/transcripts500new.txt -fo $DIR$EXT/transcripts500new.fasta