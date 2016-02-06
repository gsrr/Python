# -*- coding: utf-8 -*-


import sys
import time
import random
import os
import copy

#file_title="givid,id,family,sire,dam,sex,weight,length,kfactor5,BW,lice+1,logeLC,LC+1/BW,logeLD,logeweight,log10weight,logelength,log10length,logekfactor5,log10kfactor5"
DEBEG = True

file_title=""
slash = "/"
test_file = ""

def debug(msg):
    if DEBEG == True:
        print str(msg)

def readFile(path):
    data = []
    global file_title
    with open(path, "r") as fr:
        line = fr.readline()
        while line:
            line = line.strip()
            data.append(line)
            line = fr.readline()
    file_title = data[0]
    return data[1:]
    
    
def familyMap(data, paras):
    cate = paras['category']
    fmap = {}
    for line in data:
        arr = line.split(",")
        if fmap.has_key(arr[cate]):
                fmap[arr[cate]].append(line)
        else:
            fmap[arr[cate]] = [line]
    
    return fmap

def probMap(fmap, prob):
    pmap = {}
    for key in fmap.keys():
        pmap[key] = int(round(len(fmap[key]) * prob))

    return pmap

selected = []
def random_firSelectPeople(pmap, fmap):
    d1 = []
    d2 = []
    global selected
    for key in pmap.keys():
        if pmap[key] != 0:
            i = 0
            while i < pmap[key]:
                if len(fmap[key]) == 0:
                    print "No item can be selected"
                    break
                c_i = random.randint(0, len(fmap[key]) - 1)
                item = fmap[key].pop(c_i)
                if item not in selected:
                    d1.append(item)
                    selected.append(item)
                    i += 1

        for i in range(0, len(fmap[key])):
            d2.append(fmap[key].pop())
        for i in range(len(selected)):
            d2.append(selected[i])
    return d1, d2

def firSelectPeople(pmap, fmap):
    d1 = []
    d2 = []
    for key in pmap.keys():
        if pmap[key] != 0:
            for i in range(pmap[key]):
                c_i = random.randint(0, len(fmap[key]) - 1)
                d1.append(fmap[key].pop(c_i))

        for i in range(0, len(fmap[key])):
            d2.append(fmap[key].pop())
    return d1, d2

def related_output(folder,index, d1, d2):
    file1 = folder + slash + "pheno_v" + str(index) + ".csv"
    file2 = folder + slash + "pheno_except_v" + str(index) + ".csv"
    print file1, file2
    with open(file1, "w") as fw:
        fw.write(file_title + "\n")
        for line in d1:
            fw.write(line + "\n")
    with open(file2, "w") as fw:
        fw.write(file_title + "\n")
        for line in d2:
            fw.write(line + "\n")

def random_related_pop(index, paras): 
    global test_file
    data = readFile(test_file)
    fmap = familyMap(data, paras)
    pmap = probMap(fmap, paras['prob'])
    d1, d2 = random_firSelectPeople(pmap, fmap)
    print len(data), len(d1), len(d2)
    related_output("related_pop", index, d1, d2)

def related_pop(index, paras): # first
    global test_file
    data = readFile(test_file)
    fmap = familyMap(data, paras)
    pmap = probMap(fmap, paras['prob'])
    d1, d2 = firSelectPeople(pmap, fmap)
    print len(data), len(d1), len(d2)
    related_output("related_pop", index, d1, d2)


def sumProb(fmap, prob):
    sum_prob = 0
    for key in fmap.keys():
        sum_prob += len(fmap[key])
    return int(round(sum_prob * prob))
    

def randomalize(class_pool):
    for i in range(len(class_pool)):
        j = random.randint(i, len(class_pool)-1)
        temp = class_pool[i]
        class_pool[i] = class_pool[j]
        class_pool[j] = temp

def sumNodes(class_pool, nodes, fmap):
    sum_nodes = 0
    for num in nodes:
        sum_nodes += len(fmap[class_pool[num]])

    return sum_nodes


def nodesInOldClass(nodes, old_class):
    for ns in old_class:
        if len(ns) != len(nodes):
            continue
        for item in ns:
            if item not in nodes:
                continue
        return True
   
    return False

def random_selectClassFromPool(class_pool, nodes, fmap, total, old_class, index):
    sum_nodes = sumNodes(class_pool, nodes, fmap) 
    if sum_nodes == total:
        return 0

    if sum_nodes > total:
        return 1
    
    i = index
    while i < len(class_pool):
        if (i not in nodes) and (i not in old_class):
            nodes.append(i)
            debug(nodes)
            ret = random_selectClassFromPool(class_pool, nodes,  fmap, total, old_class, i+1)
            if ret == 0:
                return 0
            nodes.pop()
        i += 1

def selectClassFromPool(class_pool, nodes, fmap, total, old_class):
    sum_nodes = sumNodes(class_pool, nodes, fmap) 
    if sum_nodes == total:
        if nodesInOldClass(nodes, old_class):
            return 2
        return 0

    if sum_nodes > total:
        return 1
    

    for i in range(len(class_pool)):
        if i not in nodes:
            nodes.append(i)
            ret = selectClassFromPool(class_pool, nodes,  fmap, total, old_class)
            if ret == 0:
                return 0
            nodes.pop()

def secOutput(folder, index, nodes, class_pool, fmap):
    file1 = folder + slash + "pheno_v" + str(index) + ".csv"
    file2 = folder + slash + "pheno_except_v" + str(index) + ".csv"
    print file1, file2
    fw1 = open(file1, "w")
    fw2 = open(file2, "w")

    fw1.write(file_title + "\n")
    fw2.write(file_title + "\n")
    keys = copy.copy(class_pool)
    for num in nodes:
        key = keys[num]
        for line in fmap[key]:
            fw1.write(line + "\n")
    
    for i in range(0, len(keys)):
        if i not in nodes:
            for line in fmap[keys[i]]:
                fw2.write(line + "\n")
    fw1.close()
    fw2.close()

def random_unrelated_pop(index, paras):  # second
    global test_file
    old_class_list = paras['old_class']
    data = readFile(test_file)
    fmap = familyMap(data, paras)
    select_total = sumProb(fmap, paras['prob'])
    class_pool = fmap.keys()
    randomalize(class_pool)
    nodes = []
    random_selectClassFromPool(class_pool, nodes,  fmap, select_total, old_class_list, 0)
    if nodes:
        debug(str(nodes))
        secOutput("unrelated_pop", index, nodes, class_pool, fmap)
        old_class_list += nodes
    else:
        print "can not find class combination!!"

def unrelated_pop(index, paras):  # second
    global test_file
    old_class_list = paras['old_class']
    data = readFile(test_file)
    fmap = familyMap(data, paras)
    select_total = sumProb(fmap, paras['prob'])
    class_pool = fmap.keys()
    randomalize(class_pool)
    nodes = []
    selectClassFromPool(class_pool, nodes,  fmap, select_total, old_class_list)
    if nodes:
        secOutput("unrelated_pop", index, nodes, class_pool, fmap)
        old_class_list.append(copy.copy(nodes))
    else:
        print "can not find class combination!!"

        
def third_write(data, num, i):
    path = "random_pop/pheno_v" + str(num + 1) 
    with open(path, "a") as fw:
        fw.write(data[i] + "\n")

def third_write_exp(data, length, i):
    for j in range(int(len(data)/length)):
        path = "random_pop/pheno_except_v" + str(j + 1) 
        if j != (i//length):
            open(path, "a").write(data[i] + "\n")

def random_pop(paras): 
    prob = paras['prob']
    data = readFile(test_file)
    randomalize(data)
    base = 0
    length = len(data) * prob
    
    for i in range(len(data)):
        third_write(data, int(i//length), i)
        third_write_exp(data, length, i)    
        
if __name__ == "__main__":
    if len(sys.argv) < 4:
        print "format error , example: python family_choose.py related_pop 0.2 5 2"   # 0.2 is probability, 5 is N=5, 2 is family column, start from 0, 1, 2...
        sys.exit(0)
    test_file = "com_pheno.csv"
    paras = {}
    paras['op'] = sys.argv[1]
    paras['prob'] = float(sys.argv[2])
    paras['n'] = int(sys.argv[3])
    paras['category'] = int(sys.argv[4])
    paras['old_class'] = []
    try:
        os.mkdir("random_pop")
        os.mkdir("related_pop")
        os.mkdir("unrelated_pop")
    except:
        pass
    func = getattr(sys.modules[__name__], paras['op'])
    if paras['op'] == "random_select" :
        func(paras)
    else:
        for i in range(paras['n']):
            func(i+1, paras)
