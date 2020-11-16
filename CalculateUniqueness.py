# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 23:15:17 2020

@author: Sachin Gowda
"""


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

files_per_folder = {}
min_index_SRAM='A'
max_index_SRAM='B'
for k in [chr(i) for i in range(ord(min_index_SRAM), ord(max_index_SRAM) + 1)]:
    folder = 'uniqueness/' + k
    files = read_folder(folder)
    files_per_folder[k] = files

inter_hd = []
for a, b in itertools.combinations(files_per_folder, 2):
    files1 = files_per_folder[a]
    files2 = files_per_folder[b]
    
    dis = h.calculate_inter_hamming_distance(files1, files2, length=2089248)
    inter_hd.append(dis)
    print("Inter hamming distance is",  dis, "%")

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ['dis' ]
students = dis
ax.bar(langs,students)
plt.show()





