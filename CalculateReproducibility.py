import os
import itertools
from hamming_distance import Analyzer
from PUF import Tools, Analyzer, DataRemanenceCalculator
import distance
h = Analyzer.Analyzer()


def read_folder(folder):
    result = []
    for f in os.listdir(folder + "/"):
        file = folder + "/" + f
        if os.path.isdir(file):
            result.extend(read_folder(file))
        else:
            if not file.endswith(".DS_Store"):
                result.append(read_file(file))
    return result


def read_file(file):
    return Tools.read_bits_from_file_and_merge(file)


min_index_SRAM='A'
max_index_SRAM='A'
files_per_folder = {}

for k in [chr(i) for i in range(ord(min_index_SRAM), ord(max_index_SRAM) + 1)]:
    folder = 'reproducibility/' + k
    files = read_folder(folder)
    files_per_folder[k] = files
total = 0
count = 0
highest = 0
highest_pct = 0
length = 2089248
lowest = length
lowest_pct = 101
distances = {}
if isinstance(files, dict):
    print('i')
    for a1, b1 in itertools.combinations(files, 2):
        a = files[a1]
        b = files[b1]
        if len(a) != length and len(b) != length:
            continue
        dis = distance.hamming(a, b)
        pct = (dis / length) * 100
        total += pct
        count += 1
        name = a1 + "-" + b1
        distances[name] = pct
        if highest < dis:
            highest = dis
            highest_pct = pct
        if lowest > dis:
            lowest = dis
            lowest_pct = pct
else:

    for a, b in itertools.combinations(files, 2):
        
        if len(a) != length and len(b) != length:
            continue
        dis = distance.hamming(a, b)
        pct = (dis / length) * 100
        
        total += pct
        count += 1
        if highest < dis:
            highest = dis
            highest_pct = pct
        if lowest > dis:
            lowest = dis
            lowest_pct = pct
            # print(str(dis) + ", " + str(pct) + "%")
    average = total / count if count > 0 else 0
    print("avererage intra hamming distance of MWG5 is =", average,"%")
    
import matplotlib.pyplot as plt
import numpy as np
#fig = plt.figure()
#ax = fig.add_axes([0,0,1,1])
#plt.bar(average, height=1,width=1, align='center')
#langs = ['Average' ]
#students = average
#ax.bar(langs,students)
#plt.show()
fig = plt.figure()
objects = ('MWG-5')
#y_pos = np.arange(len(objects))
performance = [average]
langs = ['Average' ]

plt.bar(objects, performance, align='center', alpha=0.5, color = 'green')
plt.xticks(objects)
plt.ylabel('Hamming distance in percentage')
plt.title('intra hamming distnace of MWG-5')

plt.show()
fig.savefig('intra hamming distance MWG5.png')



