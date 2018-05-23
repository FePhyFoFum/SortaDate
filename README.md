# SortaDate

## Introduction
This repository contains scripts that you can use at different stages to attempt to find more clock-like genes. Generally, you would use these for dating analyses with another package. 

_The results you get from these analyses are just suggestions and tools to help explore your dataset. You should be sure to examine the results carefully and not use them blindly._

## Requirements
You will minimally need `python` to run the scripts. Other than `python`, you will probably want two packages from `phyx` (see installation below) in order to run all parts of _SortaData_. 

The expected input is a set of genes that have been aligned and for which there are gene trees. Generally, we would expect these to be rooted as well. The input filetype would be fasta. If you need help converting these files, you can use `phyx` or put a feature request and we can add scripts to convert files. 

## Usage
With the input of a directory of gene alignments and corresponding gene trees, the steps of these analyses include 

1. Get the tip-to-root variation with the `get_var_length.py`
2. Get the bipartition support with `get_bp_genetrees.py`
3. Combine the results from these two runs with `combine_results.py`
4. Sort and get the list of the good genes with `get_good_genes.py`. You can give the order that you prefer the sorting so `--order 3,1,2` would mean that you want the bipartition sorted first (3=bipartition), then root-to-tip variance (1=root-to-tip variance), and then tree length (2=treelength). 

These steps are separated out with the intention that you can examine the results of each step. In each case you can type `python NAMEOFSCRIPT.py -h` to get what each argument is. The example below should also help.

## Installation
To install and use SortaDate you will need python (it is probably already on your computer if you have a Mac or Linux machine) and you will need two programs from the `phyx` set of programs (found [https://github.com/FePhyFoFum/phyx][1]). While `phyx` has many different programs, we will only need 3 and to install these, you will not need any other software other than a compiler. Because you can install only part of the `phyx` package, instructions for this will be placed here. If you would like to install all of the programs, consult the `phyx` website. 

### Installing pxlstr and pxbp
The two bits that you will need from `phyx` are `pxlstr`, `pxrmt` and `pxbp`. To install this in Mac or Linux

1. Go to [https://github.com/FePhyFoFum/phyx][2] then click the “Clone or download” and download the zip. Unzip the resulting file. 
2. Open the Terminal and change directory to the `src` directory (if you downloaded and unzipped the phyx-master.zip in your Downloads directory, on Mac you will probably run the command `cd Downloads/phyx-master/src`)
3. Run `./configure`. You will get a couple errors, probably, but you can ignore. This would be important only if you needed all of the programs in `phyx`.
4. Run `make pxlstr`, then `make pxrmt` and then `make pxbp`. Then copy the programs into your PATH (so probably `sudo cp pxlstr pxrmt pxbp /usr/local/bin/`. You will have to type your password.

### Installing SortaDate
This is trivial. Because the package is a python package, all you will need is to download the scripts here, and just run them directory from wherever you download them. You can see how to use the commands in the example below. You can grab the repository by clicking the “Clone or download” and download the zip. Unzip the resulting file and within you will find all the files. 

## Example
There is an example dataset included in the repository. This is a partial dataset from the Jarvis et al. (2014) genomic bird paper. Once you have downloaded or cloned the repository, you can run these analyses:

1. Get the root-to-tip variance with `python src/get_var_length.py examples/genes_trees/ --flend .tre.rr --outf examples/var --outg Struthio_camelus,Tinamou_guttatus`
2. Get the bipartition support with `python src/get_bp_genetrees.py examples/genes_trees/ examples/Chrono_Tent_Bird_study.new --flend .tre.rr --outf examples/bp`
3. Combine the results from these two runs with `python src/combine_results.py examples/var examples/bp --outf examples/comb`
4. Sort and get the list of the good genes with `python src/get_good_genes.py examples/comb --max 3 --order 3,1,2 --outf examples/gg`


## Additional analyses
### Rooting
If you need trees to be rooted, you can perform this in many different ways. One way that you can root these trees is with the `phyx` program `pxrr` (found [https://github.com/FePhyFoFum/phyx][3]). Since Sorta date requires 3 other phyx packages, installing the 4th should be relatively trivial by running `make pxrr` in the source directory of phyx when the other programs were made. To then move this to the path you can run `sudo cp pxrr /usr/local/bin/`.

### Conducting clock analyses
If you would like to conduct likelihood ratio tests for the clock for each of the gene trees, you may do this with `paup` and you can find that here [http://phylosolutions.com/paup-test/][4]. There are scripts included in `SortaDate` to conduct these analyses that will add the necessary paup block to the file.

## Citations
The scripts and procedures discussed here are presented in Smith et al. 2018 [So many genes, so little time: A practical approach to divergence-time estimation in the genomic era](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0197433). Plos One.

[1]:	https://github.com/FePhyFoFum/phyx
[2]:	https://github.com/FePhyFoFum/phyx
[3]:	https://github.com/FePhyFoFum/phyx
[4]:	http://phylosolutions.com/paup-test/
