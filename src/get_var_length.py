import os
import sys
import subprocess
import argparse as ap

flend = ".tre"
outg = ""
cmd1 = "pxrmt -t TREE -n OUTGROUP | pxlstr"
cmd2 = "pxlstr -t TREE"
writetofile = False

if __name__ == "__main__":
    par = ap.ArgumentParser(description="SortaDate: get_var_length | This will calculate the variation in the tip to root length for each gene tree")
    par.add_argument('di', type=str, nargs=1,metavar='DIR',help="directory where the gene trees are")
    par.add_argument('--flend', dest='fileending',help="the file endings for the gene trees")
    par.add_argument('--outg', dest='outgroups',default="",help="outgroups separated by commas")
    par.add_argument('--loc', dest='phyx_location',default="",help="where are pxlstr (and pxrmt if you have outgroups)")
    par.add_argument('--outf',dest='outf',help="the outfile")

    #parse the arguments
    args = par.parse_args()
    if args.fileending != None:
        flend = args.fileending
    di = args.di[0]
    print ("directory:",di)
    print ("file ending for trees:",flend)
    print ("outgroups:",args.outgroups)
    if args.outgroups != "":
        outg = args.outgroups
        cmd = cmd1.replace("OUTGROUP",outg)
    else:
        cmd = cmd2
    print ("phyx location:",args.phyx_location)
    if args.phyx_location != "":
        cmd = args.phyx_location+"/"+cmd
    if args.outf != None:
        print ("outfile:",args.outf)
        writetofile = True
        outf = open(args.outf,'w')

    #run the script
    for i in os.listdir(di):
        if i[-len(flend):] == flend:
            fd = di+"/"+i
            p = subprocess.Popen(cmd.replace("TREE",fd),shell=True,stdout=subprocess.PIPE)
            x = p.communicate()[0].decode("utf-8").split("\n")
            var = ""
            tl = ""
            for j in x:
                if len(j) < 3:
                    continue
                spls = j.split()
                if spls[0] == "treelength:":
                    tl = spls[1]
                elif spls[0] == "rttipvar:":
                    var = spls[1]
            if writetofile == False:
                print (i+"\t"+var+"\t"+tl)
            else:
                outf.write(i+"\t"+var+"\t"+tl+"\n")
    if writetofile == True:
        outf.close()
