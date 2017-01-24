# SortaDate

## Introduction
This repository contains scripts that you can use at different stages to attempt to find more clock-like genes. Generally, you would use these for dating analyses with another package. 

## Requirements
You will minimally need `python` to run the scripts. Other than `python`, depending on how much you want to run within _SortaData_. 

The expectation of input are a series of genes that have been aligned and for which there are gene trees. Generally, we would expect these to be rooted as well. 

## Usage
With the input of a directory of gene alignments and corresponding gene trees, the steps of these analyses include 

1. Get the tip-to-root variation with the `get_var_length.py`
2. Get the bipartition support with `get_bp_genetrees.py`
3. Combine the results from these two runs with `combine_results.py`
4. Sort and get the list of the good genes with `get_good_genes.py`

These steps are separated out with the intention that you can examine the results of each step. 

## Installation
To install and use SortaDate you will need python (it is probably already on your computer if you have a Mac or Linux machine) and you will need two programs from the `phyx` set of programs (found [https://github.com/FePhyFoFum/phyx][1]). While `phyx` has many different programs, we will only need 2 and to install these, you will not need any other software other than a compiler. Because you can install only part of the `phyx` package, instructions for this will be placed here. If you would like to install all of the programs, consult the `phyx` website. 

### Installing pxlstr and pxbp
The two bits that you will need from `phyx` are `pxlstr` and `pxbp`. To install this in Mac

### Installing SortaDate
This is trivial. Because the package is a python package, all you will need is to download the scripts here, and just run them directory from wherever you download them. You can see how to use the commands in the example below.

## Example
There is an example dataset included in the repository. This is a partial dataset from the Jarvis et al. (2014) genomic bird paper. Once you have downloaded or cloned the repository here, 

## Additional analyses
### Rooting
If you need trees to be rooted, you can perform this in many different ways. One way that you can root these trees is with `phyx` (found [https://github.com/FePhyFoFum/phyx][2]). 

### Conducting clock analyses
If you would like to conduct likelihood ratio tests for the clock for each of the gene trees, you may do this with `paup` and you can find that here [http://people.sc.fsu.edu/\~dswofford/paup\_test/][3]. There are scripts included in `SortaDate` to conduct these analyses that will add the necessary paup block to the file.

## Citations
The scripts and procedures discussed here are presented in 

[1]:	https://github.com/FePhyFoFum/phyx
[2]:	https://github.com/FePhyFoFum/phyx
[3]:	http://people.sc.fsu.edu/~dswofford/paup_test/