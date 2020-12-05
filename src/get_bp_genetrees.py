import os
import sys
import tree_reader
import subprocess
import argparse as ap

flend = ".tre"
cmd = "pxbp -t "
writetofile = False


def get_clades(tree):
    clades = []
    for i in tree.iternodes():
        if len(i.children) == 0 or i == tree:
            continue
        clades.append(set(i.lvsnms()))
    return clades


if __name__ == "__main__":
    par = ap.ArgumentParser(description="SortaDate: get_bp_genetrees | This will calculate the bipartition support for each gene tree.")
    par.add_argument('di', type=str, nargs=1,metavar='DIR',help="directory where the gene trees are")
    par.add_argument('speciestree',type=str,nargs=1,metavar='SPECIESTREE',help="the species tree")
    par.add_argument('--flend', dest='fileending',help="the file endings for the gene trees")
    par.add_argument('--loc', dest='phyx_location',default="",help="where are pxlstr (and pxrmt if you have outgroups)")
    par.add_argument('--outf',dest='outf',help="the outfile")
    args = par.parse_args()

    #parse the arguments
    if args.fileending != None:
        flend = args.fileending
    di = args.di[0]
    print ("directory:",di)
    print ("file ending for trees:",flend)
    spt = args.speciestree[0]
    print ("species tree:",spt)
    st = open(spt,"r")
    tree = tree_reader.read_tree_string(st.readline())
    st.close()
    clades = get_clades(tree)
    print ("phyx location:",args.phyx_location)
    if args.phyx_location != "":
        cmd = args.phyx_location+"/"+cmd
    if args.outf != None:
        print ("outfile:",args.outf)
        writetofile = True
        outf = open(args.outf,'w')
    
    for i in os.listdir(di):
        if i[-len(flend):] == flend:
            fd = di+"/"+i
            p = subprocess.Popen(cmd+fd,shell=True,stdout=subprocess.PIPE)
            x = p.communicate()[0].decode("utf-8").split("\n")
            var = ""
            tl = ""
            start = False
            count = 0
            for j in x:
                if "unique clades" in j:
                    start = True
                    continue
                if "TSCA:" in j:
                    break
                if start and "CLADE" in j:
                    j = j.replace("CLADE: ","")
                    spls = set(j.strip().split("\t")[0].split(" "))
                    spls.remove("")
                    tf = spls in clades
                    if tf == True:
                        count += 1
            if writetofile == False:
                print (i+"\t"+str(count/float(len(clades))))
            else:
                outf.write(i+"\t"+str(count/float(len(clades)))+"\n")
            #break
    if writetofile == True:
        outf.close()
