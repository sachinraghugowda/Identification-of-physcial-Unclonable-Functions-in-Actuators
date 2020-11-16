# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import itertools
import operator
import distance
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
#h = Analyzer.Analyzer()

ResultsPUF1 = open("binoutput_5.txt", "r")
ResultsPUF2 = open("binoutput2_5.txt", "r")
#ResultsPUF3 = open("binoutput3_5.txt", "r")
#ResultsPUF4 = open("binoutput4_5.txt", "r")
#ResultsPUF5 = open("binoutput5_1.txt", "r")

count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0
count11 = 0
count12 = 0
count13 = 0
count14 = 0
count15 = 0
count16 = 0
count17 = 0
count18 = 0
count19 = 0
count20 = 0
count21 = 0
count22 = 0
count23 = 0
count24 = 0
count25 = 0
count26 = 0 
count27 = 0
count28 = 0
count29 = 0
count30 = 0

while True:
    count = 0
    line1 = ResultsPUF1.readline()
    line2 = ResultsPUF2.readline()
 #   line3 = ResultsPUF3.readline()
 #   line4 = ResultsPUF4.readline()
   # line5 = ResultsPUF5.readline()
    print(line1)
    print(line2)
 #   print(line3)
 #   print(line4)
   # print(line5)
    if not line4: break  # EOF
    
    for (bit1a, bit1b, bit1c, bit1d) in zip(line1, line2, line3, line4):
        if ((ord(bit1a) ^ ord(bit1b)) ^ (ord(bit1c) ^ ord(bit1d))):
            count += 1
    if (count == 0):
        count0 += 1
    elif (count == 1):
        count1 += 1
    elif (count == 2):
        count2 += 1
    elif (count == 3):
        count3 += 1
    elif (count == 4):
        count4 += 1
    elif (count == 5):
        count5 += 1
    elif (count == 6):
        count6 += 1
    elif (count == 7):
        count7 += 1
    elif (count == 8):
        count8 += 1
    elif (count == 9):
        count9 += 1
    elif (count == 10):
        count10 += 1
    elif (count == 11):
        count11 += 1
    elif (count == 12):
        count12 += 1
    elif (count == 13):
        count13 += 1
    elif (count == 14):
        count14 += 1
    elif (count == 15):
        count15 += 1
    elif (count == 16):
        count16 += 1
    elif (count == 17):
        count17 += 1
    elif (count == 18):
        count18 += 1
    elif (count == 19):
        count19 += 1
    elif (count == 20):
        count20 += 1
    elif (count == 21):
        count21 += 1
    elif (count == 22):
        count22 += 1
    elif (count == 23):
        count23 += 1
    elif (count == 24):
        count24 += 1
    elif (count == 25):
        count25 += 1
    elif (count == 26):
        count26 += 1
    elif (count == 27):
        count27 += 1
    elif (count == 28):
        count28 += 1
    elif (count == 29):
        count29 += 1
    elif (count == 30):
        count30 += 1
    print("HammingDistance = " + str(count))
    
    
    
    
print("AMT of 0 Differences: " + str(count0))
print("AMT of 1 Differences: " + str(count1))
print("AMT of 2 Differences: " + str(count2))
print("AMT of 3 Differences: " + str(count3))
print("AMT of 4 Differences: " + str(count4))
print("AMT of 5 Differences: " + str(count5))
print("AMT of 6 Differences: " + str(count6))
print("AMT of 7 Differences: " + str(count7))
print("AMT of 8 Differences: " + str(count8))
print("AMT of 9 Differences: " + str(count9))
print("AMT of 10 Differences: " + str(count10))
print("AMT of 11 Differences: " + str(count11))
print("AMT of 12 Differences: " + str(count12))
print("AMT of 13 Differences: " + str(count13))
print("AMT of 14 Differences: " + str(count14))
print("AMT of 15 Differences: " + str(count15))
print("AMT of 16 Differences: " + str(count16))
print("AMT of 17 Differences: " + str(count17))
print("AMT of 18 Differences: " + str(count18))
print("AMT of 19 Differences: " + str(count19))
print("AMT of 20 Differences: " + str(count20))
print("AMT of 21 Differences: " + str(count21))
print("AMT of 22 Differences: " + str(count22))
print("AMT of 23 Differences: " + str(count23))
print("AMT of 24 Differences: " + str(count24))
print("AMT of 25 Differences: " + str(count25))
print("AMT of 26 Differences: " + str(count26))
print("AMT of 27 Differences: " + str(count27))
print("AMT of 28 Differences: " + str(count28))
print("AMT of 29 Differences: " + str(count29))
print("AMT of 30 Differences: " + str(count30))

#Graph part might break, ive only tested it for 2 cases
# example data (Fake Data Commented out)
#mu = 500 # mean of distribution
#sigma = 150 # standard deviation of distribution
##count0=3
##count1=12
##count2=45
##count3=124
##count4=245
##count5=140
##count6=90
##count7=12
##count8=56
x = [count0, count1, count2, count3, count4, count5, count6, count7, count8, count9, count10, count11, count12, count13, count14, count15, count16, count17,
     count18, count19, count20, count21, count22, count23, count24, count25, count26, count27, count28, count29, count30]

num_bins = 30
# the histogram of the data
n, bins, patches = plt.hist(x, num_bins, range=[0, 30], facecolor='green')
# add a 'best fit' line
#y = mlab.normpdf(bins, mu, sigma)
fig = plt.figure()
plt.bar(bins,x,width=1, color='g')
plt.plot(bins, x, 'r--', figure = fig)
plt.xlabel('Hamming Distance')
plt.ylabel('Amount of Similar Bit Differences')
plt.title(r'Histogram of Intra-Hamming Distances')

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()
fig.savefig('plot.png')
