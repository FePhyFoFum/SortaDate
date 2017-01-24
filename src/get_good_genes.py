import sys
import operator
import argparse as ap


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "python "+sys.argv[0]+ " Var_CT_BP.txt"
        sys.exit(0)
    tuples = []
    inf = open(sys.argv[1],"r")
    for i in inf:
        spls = i.strip().split()
        tuples.append((spls[0],float(spls[1]),float(spls[2]),1/(float(spls[-1])+0.0000001)
            ,float(spls[-1])))
    inf.close()
    list1 = sorted(tuples,key=operator.itemgetter(3,1,2))
    for i in list1[0:4]:
        print i

