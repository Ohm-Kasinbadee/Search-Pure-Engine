import csv
import ast
import time
import pandas
import pandas as pd
import numpy as np
import psutil

def binarySearch(alist, item):
  CountBinay = 0
  first = 0
  last = len(alist)-1
  found = False
  
  while first<=last and not found:
    midpoint = (first + last)//2
    if alist[midpoint] == item:
      found = True
    else:
      if item < alist[midpoint]:
      	CountBinay += 1
      	last = midpoint - 1
      else:
      	CountBinay += 1
      	first = midpoint + 1
          
  return found,CountBinay


def InvertedIndex(InputData):
	start_time = time.time()

	arrayURL = []
	arrayList = []
	CutarrayList = []

	URLDatas = []
	arrayURLDatas = []
	CutarrayListDatas = []
	times = ''
	timesFile = []
	CountBinay = []
	number = []

	URL = pandas.read_csv('url1000.csv')
	for i in range(0,len(URL)):
	# for i in range(0,460):
		arrayURL.append(URL['url'][i])

	with open('DataSets.csv', 'r',encoding="utf8", errors='ignore') as csvfile:
		start_time_FileURL = time.time()
		readCSV = csv.reader(csvfile, delimiter=',')

		for row in readCSV:
			arrayList.append(row)


		for col in arrayList:
			CutToken = list(set(col))
			SortToken = sorted(CutToken)
			CutarrayList.append(SortToken)

	# print(arrayList)

	for data in range(0,len(CutarrayList)):
		if binarySearch(CutarrayList[data], InputData)[0] == True:
			URLDatas.append(data)
			arrayURLDatas.append(arrayURL[data])
			CutarrayListDatas.append(CutarrayList[data])
			CountBinay.append(binarySearch(CutarrayList[data], InputData)[1]) 
			number.append(data+1)
			timesFile.append((" %s seconds " %  (time.time() - start_time_FileURL)))
	
	CountLoop = 0
	for x in range(0,len(CountBinay)):
		CountLoop += CountBinay[x]

	time_2f = '%.2f' % (time.time() - start_time)
	times = ((" %s seconds " % time_2f ))
	# times = ((" %s seconds " %  (time.time() - start_time)))

	cpu = str(psutil.cpu_percent(interval=1))
	memory = str(psutil.swap_memory()[3])
	disk = str(psutil.disk_usage('/')[3])

	return list(arrayURLDatas), times, CountLoop, CountBinay, list(number), timesFile, cpu, memory, disk

def PositionIndex(InputData):
	start_time = time.time()

	lowInput = InputData.lower()
	SplitInput = lowInput.split()

	arrayList = []
	arrayURL = []
        

	URL = pandas.read_csv('url1000.csv')
	# for i in range(0,len(URL)):
	for i in range(0,460):
  		arrayURL.append(URL['url'][i])


	with open('DataSet.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			arrayList.append(row)

	dict = {}
	for x in range(0,len(arrayList)):
		dicts = {}
		# print(x)
		# print('---------')
		DataSetArray = np.array(arrayList[x])

		for y in range(0,len(SplitInput)):
			# print(y)
			dicts[SplitInput[y]] = np.concatenate(np.where(DataSetArray == SplitInput[y])).tolist()
		# print('########')
		dict[x] = dicts

	time_2f = '%.2f' % (time.time() - start_time)
	times = ((" %s seconds " % time_2f ))
	cpu = str(psutil.cpu_percent(interval=1))
	memory = str(psutil.swap_memory()[3])
	disk = str(psutil.disk_usage('/')[3])

	return dict, SplitInput, arrayURL, times, cpu, memory, disk


# print(len(InvertedIndex('to')[0]))
# InvertedIndex('to')
# print(len(InvertedIndex('to')[4]))
# print(InvertedIndex('to')[3])
# print(InvertedIndex('to'))
# print(PositionIndex('com to be one'))
# print(PositionIndex('com to')[0])

