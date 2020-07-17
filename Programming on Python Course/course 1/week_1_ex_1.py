import sys

digit_string = sys.argv[1]

# print(type(digit_string)) # <type 'str'>

_sum = 0
for i in digit_string:
    i = int(i)
    _sum += i

print(_sum)

# print(sum([int(x) for x in sys.argv[1]]))
