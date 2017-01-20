# SortaDate

## Introduction
This repository contains scripts that you can use at different stages to attempt to find more clock-like genes. Generally, you would use these for dating analyses with another package. 

## Requirements
You will minimally need `python` to run the scripts. Other than `python`, depending on how much you want to run within _SortaData_. 

The expectation of input are a series of genes that have been aligned and for which there are gene trees. Generally, we would expect these to be rooted as well. 

## Usage
With the input of a directory of gene alignments and corresponding gene trees, the steps of these analyses include 

1. Get the tip-to-root variation with the `get_var_length.py`

### Rooting
If you need trees to be rooted, you can perform this in many different ways. One way that you can root these trees is with `phyx` (found [https://github.com/FePhyFoFum/phyx][1]). 

### Conducting clock analyses
If you would like to conduct likelihood ratio tests for the clock for each of the gene trees, you may do this with `paup` and you can find that here [http://people.sc.fsu.edu/\~dswofford/paup\_test/][2]. There are scripts included in `SortaDate` to conduct these analyses that will add the necessary paup block to the file.

## Citations
The scripts and procedures discussed here are presented in 

[1]:	https://github.com/FePhyFoFum/phyx
[2]:	http://people.sc.fsu.edu/~dswofford/paup_test/