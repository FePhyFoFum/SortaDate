import node
import sys,os

"""
this will create consensus trees, calculate bipartitions, calculate distances

"""

def rf_dist(tree1,tree2):
    return 0

#using rooted trees for unrooted means ignoring anything with one
def calc_biparts(tree1):
    allbiparts1 = []
    allbiparts2 = []
    for i in tree1.iternodes():
        bp1,bp2 = get_bipart(i,tree1)
        if len(bp1) < 2 or len(bp2) < 2:
            continue
        if bp1 in allbiparts1 or bp1 in allbiparts2:
            continue
        allbiparts1.append(bp1)
        allbiparts2.append(bp2)
    return allbiparts1,allbiparts2

def get_bipart(node,root):
    rtlvs = []
    for i in root.leaves_fancy():
        rtlvs.append(i.label)
    ndlvs = []
    for i in node.leaves_fancy():
        ndlvs.append(i.label)
    bp1 = set(rtlvs) - set(ndlvs)
    bp2 = set(ndlvs)
    return bp1,bp2

def calc_biparts_support(trees):
    bipartscount = []
    allbiparts1 = []
    allbiparts2 = []
    for i in range(len(trees)):
        tree = trees[i]
        abp1,abp2 = calc_biparts(tree)
        for tabp1,tabp2 in zip(abp1,abp2):
            if tabp1 in allbiparts1:
                bipartscount[allbiparts1.index(tabp1)] += 1
            elif tabp1 in allbiparts2:
                bipartscount[allbiparts2.index(tabp1)] += 1
            else:
                allbiparts1.append(tabp1)
                allbiparts2.append(tabp2)
                bipartscount.append(1)
    for i in range(len(bipartscount)):
        print allbiparts1[i],allbiparts2[i],bipartscount[i]/float(len(trees))

def get_mrca(nodes,tree):
    traceback = []
    first = nodes[0]
    while first != tree:
        first = first.parent
        traceback.append(first)
        if first.parent == None:
            break
    curmrca = nodes[0].parent
    for i in nodes:
        if i == nodes[0]:
            continue
        curmrca = mrca_recurs(curmrca,traceback,i)
    return curmrca

def mrca_recurs(node1,path1,node2):
    path = path1[path1.index(node1):]
    parent = node2
    mrca = None
    while parent != None:
        if parent in path:
            mrca = parent
            break
        parent = parent.parent
    return mrca

#assumes an ultrametric tree
def scale_root(tree,age):
    for i in tree.iternodes(order="postorder"):
        i.set_height()
    oldroot = tree.height
    tree.height = age
    for i in tree.iternodes(order="postorder"):
        if i != tree and len(i.children) > 0:
            i.height = (i.height/oldroot) * tree.height
    for i in tree.iternodes(order="postorder"):
        if len(i.children) > 0:
            for j in i.children:
                j.length = i.height - j.height
