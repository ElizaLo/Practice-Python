'''
Below, we have provided a list of lists. Use indexing to assign the element ‘horse’ to the variable name idx1.
'''
animals = [['cat', 'dog', 'mouse'], ['horse', 'cow', 'goat'], ['cheetah', 'giraffe', 'rhino']]

idx1 = animals[1][0]


'''
Using indexing, retrieve the string ‘willow’ from the list and assign that to the variable plant.
'''
data = ['bagel', 'cream cheese', 'breakfast', 'grits', 'eggs', 'bacon', [34, 9, 73, []], [['willow', 'birch', 'elm'], 'apple', 'peach', 'cherry']]

plant = data[7][0][0]


'''
Extract the value associated with the key color and assign it to the variable color. Do not hard code this.
'''
info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }

color = info['personal_data']['physical_features']['color']


'''
Below, we have provided a list of lists that contain information about people. 
Write code to create a new list that contains every person’s last name, and save that list as last_names.
'''
info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]

last_names = []
for person in info:
    last_names.append(person[1])


'''
Below, we have provided a list of lists named L. 
Use nested iteration to save every string containing “b” into a new list named b_strings.
'''
L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]

b_strings = []

for lst in L:
    for word in lst:
        if 'b' in word:
            b_strings.append(word)


'''
Using map, create a list assigned to the variable greeting_doubled that doubles each element in the list lst.
'''
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

greeting_doubled = map(lambda x: x * 2, lst)


'''
Below, we have provided a list of strings called abbrevs. 
Use map to produce a new list called abbrevs_upper that contains all the same strings in upper case.
'''
abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]

abbrevs_upper = map(lambda ch: ch.upper(), abbrevs)


'''
Write code to assign to the variable filter_testing all the elements in lst_check that have a w in them using filter.
'''
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

filter_testing = filter(lambda word: 'w' in word.lower(), lst_check)


'''
Using filter, filter lst so that it only contains words containing the letter “o”.
Assign to variable lst2. Do not hardcode this.
'''
lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]

lst2 = filter(lambda word: 'o' in word, lst)


'''
The for loop below produces a list of numbers greater than 10. 
Below the given code, use list comprehension to accomplish the same thing. Assign it the the variable lst2. 
Only one line of code is needed.
'''
L = [12, 34, 21, 4, 6, 9, 42]
lst = []
for x in L:
    if x > 10:
        lst.append(x)

lst2 = [num for num in L if num > 10]

print(lst)


'''
Write code to assign to the variable compri all the values of the key name in any of the sub-dictionaries in the 
dictionary tester. Do this using a list comprehension.
'''
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}

compri = [d['name'] for d in tester['info'] ]


'''
Below we have provided two lists of numbers, L1 and L2. Using zip and list comprehension, create a new list, L3, 
that sums the two numbers if the number from L1 is greater than 10 and the number from L2 is less than 5. 
This can be accomplished in one line of code.
'''
L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

L3 = [x1 + x2 for (x1, x2) in zip(L1, L2) if x1 > 10 and x2 < 5]
