my_str = "MICHIGAN"

for achar in my_str:
    print(achar)

several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]

for thing in several_things:
    print(thing)

for thing in several_things:
    print(type(thing))

str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

# Write your code here.
for item in str_list:
    print(len(item))

original_str = "The quick brown rhino jumped over the extremely lazy fox."

num_chars = 0
for achar in original_str:
    num_chars += 1

print(num_chars)

addition_str = "2+5+10+20"

addition_str = addition_str.split('+')

sum_val = 0
for num in addition_str:
    num = int(num)
    sum_val += num

print(sum_val)


week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"

week_temps_f = week_temps_f.split(',')

avg_temp = 0
count = 0
for temp in week_temps_f:
    temp = float(temp)
    count += 1
    avg_temp += temp

avg_temp = avg_temp / count
print(avg_temp)

nums = range(68)
print(nums)

original_str = "The quick brown rhino jumped over the extremely lazy fox"
original_str_ = original_str.split()
num_words_list = list()

for word in original_str_:
    word = len(word)
    num_words_list.append(word)

print(num_words_list)

lett = ''

for i in range(7):
    lett = lett + 'b'
