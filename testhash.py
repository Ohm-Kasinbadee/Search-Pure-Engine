import csv
import ast
import time
import pandas
import pandas as pd
import numpy as np
import psutil

global str

def rehash(oldhash, table_size):
    return (oldhash+1) % table_size

def weighted_ord_hash(string, table_size):
    hash_val = 0
    for position in range(len(string)):
        hash_val = hash_val + (ord(string[position]) * position)
    return hash_val % table_size


def lp_hash(item_list, table_size):
    
    lp_hash_table = dict([(i,None) for i,x in enumerate(range(table_size))])
    
    for item in item_list:
        i = weighted_ord_hash(item, table_size)
        # print("%s hashed == %s \n" %(item, i))
        if lp_hash_table[i] == None:
            lp_hash_table[i] = item
        elif lp_hash_table[i] != None:
            # print("Collision, attempting linear probe \n")
            next_slot = rehash(i, table_size)
            # print("Setting next slot to %s \n" % next_slot)
            while lp_hash_table[next_slot] != None:
                next_slot = rehash(next_slot, len(lp_hash_table.keys()))
                # print("Next slot was not empty, trying next slot %s \n" % next_slot)
            if lp_hash_table[next_slot] == None:
                lp_hash_table[next_slot] = item
    return lp_hash_table

def get_key(input, dict): 
    for key, value in dict.items(): 
         if input == value: 
             return key 
  
    return "key doesn't exist"

def hashIndex(InputData):
    start_time = time.time()

    lowInput = InputData.lower()
    SplitInput = lowInput.split()
    # SplitInput = ['come' ,'to', 'home']

    arrayURL = []
    arrayList = []
    CutarrayList = []

    URL = pandas.read_csv('url1000.csv')
    # for i in range(0,len(URL)):
    for i in range(0,5):
        arrayURL.append(URL['url'][i])

    with open('DataSet.csv') as csvfile:
        start_time_FileURL = time.time()
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            arrayList.append(row)

        for col in arrayList:
            CutToken = list(set(col))
            SortToken = sorted(CutToken)
            CutarrayList.append(SortToken)

    lists = []

    # for x in range(0,len(CutarrayList)):
    # for x in range(0,5):
    #     CutarrayList[x] = [str for str in CutarrayList[x] if str]
    #     lists.append(lp_hash(CutarrayList[x], 3400))


    with open("data.txt", "r") as f:
        for line in f:
            # print(list(ast.literal_eval(line.strip())))
            lists = list(ast.literal_eval(line.strip()))

    # print(lists)
        
    dictAll = {}
    for x in range(0,len(lists)):
        dicts = {}
        for y in range(0,len(SplitInput)):
            if get_key(SplitInput[y],lists[x]) != "key doesn't exist":
                dicts[SplitInput[y]] = True
            else:
                dicts[SplitInput[y]] = False
        dictAll[x] = dicts

    time_2f = '%.2f' % (time.time() - start_time)
    times = ((" %s seconds " % time_2f ))
    # times = ((" %s seconds " %  (time.time() - start_time)))

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.swap_memory()[3]
    disk = psutil.disk_usage('/')[3]

    return dictAll ,arrayURL ,times, cpu, memory, disk


print(hashIndex('come'))










