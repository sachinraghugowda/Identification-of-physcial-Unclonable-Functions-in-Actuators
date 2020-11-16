# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 01:14:01 2020

@author: Sachin Gowda
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
objects = ('MWG 1', 'MWG 2' , 'MWG 3', 'MWG 4', 'MWG 5')
y_pos = np.arange(len(objects))
performance = [28.936, 30.613, 28.80, 31.776, 28.409]

plt.bar(y_pos, performance, align='center', alpha=0.5, color= 'red')
plt.xticks(y_pos, objects)
plt.ylabel('inter-hamming distance in percentage')
plt.title('inter-hamming distance in MWGs')

plt.show()
fig.savefig('inter hamming distance in MWGs(uniqueness).png')