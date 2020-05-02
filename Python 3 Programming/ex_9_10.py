verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]

ing = []
for verb in verbs:
    verb = verb + 'ing'
    ing.append(verb)

print(ing)


numbs = [5, 10, 15, 20, 25]
newlist = []

for number in numbs:
    number +=5
    newlist.append(number)

print(newlist)


numbs = [5, 10, 15, 20, 25]
numbs.remove(5)
numbs.append(30)


lst_nums = [4, 29, 5.3, 10, 2, 1817, 1967, 9, 31.32]

larger_nums = []

for number in lst_nums:
    number *= 2
    larger_nums.append(number)
