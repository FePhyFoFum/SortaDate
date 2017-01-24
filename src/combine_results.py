import sys
import argparse as ap

if __name__ == "__main__":
    par = ap.ArgumentParser(description="SortaDate: combine_results | This will combine the results from var and bp analyses.")
    par.add_argument('var_file',nargs=1,metavar="VAR",help="the var file created from get_var_length.py")
    par.add_argument('bp_file',nargs=1,metavar="BP",help="the bp file created from get_bp_genetrees.py")
    par.add_argument('--outf',dest='outf',help="the outfile")
    args = par.parse_args()
    
    var = args.var_file[0]
    bp = args.bp_file[0]
    inf1 = open(var,"r")
    inf3 = open(bp,"r")
    fl = {}
    for i in inf1:
        spls = i.strip().split("\t")
        fl[spls[0]] = spls[1:]
    inf1.close()
    for i in inf3:
        spls = i.strip().split("\t")
        fl[spls[0]].append(spls[-1])
    inf3.close()
    for i in fl:
        print i+"\t"+"\t".join(fl[i])
