import sys
import operator
import argparse as ap

writetofile = False
maxn = 4
first = 3
second = 1
third = 2
ordd = {1:"root-to-tip variance", 2:"treelength", 3:"bipartition"}

if __name__ == "__main__":
    par = ap.ArgumentParser(description="SortaDate: get_good_genes | This will sort the results from combine analyses.")
    par.add_argument('comb_file',nargs=1,metavar="COMB",help="the comb file created from combine_results.py")
    par.add_argument('--order',dest='order',help="what parts are most important (list three in order like 1,2,3 where 1=root-to-tip variance, 2=treelength, 3=bipartition)")
    par.add_argument('--max', dest='max',help="maximum number of results")
    par.add_argument('--outf',dest='outf',help="the outfile")
    args = par.parse_args()

    if args.order != None:
        od = args.order.split(",")
        first = int(od[0])
        second = int(od[1])
        third = int(od[2])
    
    
    print ("order:",ordd[first],ordd[second],ordd[third])

    if args.max != None:
        maxn = int(args.max)

    if args.outf != None:
        print ("outfile:",args.outf)
        writetofile = True
        outf = open(args.outf,'w')
        
    tuples = []
    inf = open(args.comb_file[0],"r")
    for i in inf:
        spls = i.strip().split()
        tuples.append((spls[0],float(spls[1]),float(spls[2]),-float(spls[-1])))
    inf.close()
    list1 = sorted(tuples,key=operator.itemgetter(first,second,third))
    if writetofile == False:
        print ("name root-to-tip_var treelength bipartition")
    elif writetofile == True:
        outf.write("name root-to-tip_var treelength bipartition\n")
    for i in list1[0:maxn]:
        if writetofile == False:
            print (i[0],i[1],i[2],float(abs(i[3])))
        elif writetofile == True:
            outf.write(i[0]+" "+str(i[1])+" "+str(i[2])+ " " +str(float(abs(i[3])))+"\n")
    if writetofile == True:
        outf.close()

