#Extracting Data With Regular Expressions

import re

handle = open('regex_sum_398214.txt')

print( sum( [ float(num) for num in re.findall('[0-9]+',handle.read()) ] ) )
