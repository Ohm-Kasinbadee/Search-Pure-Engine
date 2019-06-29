import re
import csv
import ast
import time
import pandas
import pandas as pd
import numpy as np
import psutil

def WildCardsearch(InputData):
	start_time = time.time()

	arrayList = []
	arrayURL = []
	CutarrayList = []
        
	URL = pandas.read_csv('url1000.csv')
	# for i in range(0,len(URL)):
	for i in range(0,460):
  		arrayURL.append(URL['url'][i])

	with open('DataSet.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			arrayList.append(row)

		for col in arrayList:
			CutToken = list(set(col))
			SortToken = sorted(CutToken)
			CutarrayList.append(SortToken)

	regex = re.compile(InputData)
	# l = ['this', 'is', 'just', 'a', 'test','thia','thai']
	Found = []
	# for x in range(0,len(URL)):
	for x in range(0,460):
		matches = [string for string in CutarrayList[x] if re.match(regex, string)]
		Found.append(matches)
	# print(matches)

	# for x in range(0,len(Found)):
	# 	print(Found[x])

	time_2f = '%.2f' % (time.time() - start_time)
	times = ((" %s seconds " % time_2f ))
	cpu = str(psutil.cpu_percent(interval=1))
	memory = str(psutil.swap_memory()[3])
	disk = str(psutil.disk_usage('/')[3])

	return Found, arrayURL, times, cpu, memory, disk

# print(WildCardsearch('c.m'))
# WildCardsearch('o.e')
# 
													    

													
													

