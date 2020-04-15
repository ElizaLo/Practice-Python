# Extracting Data With Regular Expressions

import re

#handle = open('regex_sum_42.txt')
handle = open('regex_sum_398214.txt')

counter = 0
numlist = list()

for line in handle:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) == 0: continue
    for num in x:
        num = float(num)
        numlist.append(num)
        counter = counter + 1

s = sum(numlist)

#print(counter)
#print(numlist)
print(s)
