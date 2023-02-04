import matplotlib.pyplot as plt
import csv
import os
import numpy as np
  

fileNames = ['1000_words.csv'  ,'10000_words.csv',
     '10000000_words.csv'  , '50000000_words.csv',
     '100000000_words.csv', '200000000_words.csv',
     '300000000_words.csv']

fileSize = [1000, 10000, 10000000, 50000000, 100000000, 200000000, 300000000]

normalizedFileSize = []
value = 0
for item in fileSize:
    value = item / 10000000
    normalizedFileSize.append(value)
    # print(value)

totalTime = []

partialTime = 0
items = 0

fig, axes = plt.subplots()

dir10Cores = os.getcwd() + "/outputs/parallel/10core/decoding"
dir20Cores = os.getcwd() + "/outputs/parallel/20core/decoding"
dir40Cores = os.getcwd() + "/outputs/parallel/40core/decoding"
dir50Cores = os.getcwd() + "/outputs/parallel/50core/decoding"
dir100Cores = os.getcwd() + "/outputs/parallel/100core/decoding"

serialPath = os.getcwd() + "/outputs/serial/decoding"

# '''1 CORE (serial)'''
# for filename in fileNames:
#     if "words" in filename:
#         with open(os.path.join(serialPath,filename), 'r') as csvfile:
#             plots = csv.reader(csvfile, delimiter = ',')
#             next(plots, None)
#
#             for row in plots:
#                 partialTime += float(row[1])
#                 items += 1
#
#             partialTime = partialTime / items
#             #partialTime = partialTime / 60
#             #print(partialTime)
#             items = 0
#             totalTime.append(partialTime)
#             partialTime = 0
#
# axes.plot(totalTime,normalizedFileSize, label="1 core", linestyle=":")
# totalTime = []
# partialTime = 0

'''10 CORES'''
for filename in fileNames:
    if "words" in filename:
        with open(os.path.join(dir10Cores,filename), 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter = ',')
            next(plots, None)

            for row in plots:
                partialTime += float(row[1])
                items += 1

            partialTime = partialTime / items
            #partialTime = partialTime / 60
            #print(partialTime)
            items = 0
            totalTime.append(partialTime)
            partialTime = 0

axes.plot(totalTime,normalizedFileSize, label="10 cores", linestyle=":")
totalTime = []
partialTime = 0

'''20 CORES'''
for filename in fileNames:
    if "words" in filename:
        with open(os.path.join(dir20Cores,filename), 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter = ',')
            next(plots, None)

            for row in plots:
                partialTime += float(row[1])
                items += 1

            partialTime = partialTime / items
            #partialTime = partialTime / 60
            #print(partialTime)
            items = 0
            totalTime.append(partialTime)
            partialTime = 0

axes.plot(totalTime,normalizedFileSize, label="20 cores", linestyle=":")
totalTime = []
partialTime = 0

'''40 CORES'''
for filename in fileNames:
    if "words" in filename:
        with open(os.path.join(dir40Cores,filename), 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter = ',')
            next(plots, None)

            for row in plots:
                partialTime += float(row[1])
                items += 1

            partialTime = partialTime / items
            #partialTime = partialTime / 60
            #print(partialTime)
            items = 0
            totalTime.append(partialTime)
            partialTime = 0

axes.plot(totalTime,normalizedFileSize, label="40 cores", linestyle=":")
totalTime = []
partialTime = 0

'''50 CORES'''
for filename in fileNames:
    if "words" in filename:
        with open(os.path.join(dir50Cores,filename), 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter = ',')
            next(plots, None)

            for row in plots:
                partialTime += float(row[1])
                items += 1

            partialTime = partialTime / items
           # partialTime = partialTime / 60
            #print(partialTime)
            items = 0
            totalTime.append(partialTime)
            partialTime = 0

axes.plot(totalTime,normalizedFileSize, label="50 cores", linestyle=":")
totalTime = []
partialTime = 0

'''100 CORES'''
for filename in fileNames:
    if "words" in filename:
        with open(os.path.join(dir100Cores,filename), 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter = ',')
            next(plots, None)

            for row in plots:
                partialTime += float(row[1])
                items += 1

            partialTime = partialTime / items
           # partialTime = partialTime / 60
            #print(partialTime)
            items = 0
            totalTime.append(partialTime)
            partialTime = 0

axes.plot(totalTime,normalizedFileSize, label="100 cores", linestyle=":")
totalTime = []
partialTime = 0

'''for filename in fileNames:
    if "Sparse" in filename:
        with open(os.path.join(serialPath,filename), 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter = ',')
            next(plots, None)

            for row in plots:
                partialTime += float(row[3])
                items += 1

            partialTime = partialTime / items
            #partialTime = partialTime / 60
            print(partialTime)
            items = 0
            totalTime.append(partialTime)
            partialTime = 0

axes.plot(totalTime,normalizedFileSize, label="sparse data")
'''
axes.legend()
axes.set_ylabel('Word count in 10000000')
axes.set_xlabel('total time(seconds)')
axes.set_ylim(0,35)
axes.set_xlim(0.0, 90.0)

#axes.grid(True)
axes.set_title("ramp-up comparison of data with different cores")

plt.savefig('ramp-up-comparison-of-data-with-different-cores')

plt.show()